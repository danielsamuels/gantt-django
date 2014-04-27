var ganttApp = angular.module('ganttApp', [])

ganttApp.controller('DataCtrl', function($scope, $http) {

    $http.get('/data/').success(function(data) {
        // The front-end calendar is broken up into blocks, blocks of emptyness and blocks of 'stuff'.
        // We need to work out how to arrange all of these blocks on a per-user basis. Example below.
        // (I know this is likely a horrible implementation, but I can't think of anything better right now)
        //
        // Empty (5)
        // Item (6)
        // Item (5)
        // Empty (1)
        // Item (4)

        // Assign all XHR data to scope. (Might be better to not do this?)
        for (item in data) {
            $scope[item] = data[item];
        }

        // Generate a full date range.
        $scope.dates = []
        $scope.months = {}

        working_date = Date.parse(data.start_date).moveToFirstDayOfMonth();
        start_date = working_date;
        end_date = Date.parse(data.end_date).moveToLastDayOfMonth().addDays(1);

        while (working_date.isBefore(end_date)) {
            date_clone = working_date.clone()

            // Add the new date to the dates scope.
            $scope.dates.push(date_clone);

            // Build up the months array.
            month_str = date_clone.toString('yyyy-MM');

            if ($scope.months[month_str] === undefined) {
                $scope.months[month_str] = {
                    'human': date_clone.toString('MMMM yyyy'),
                    'days': Date.getDaysInMonth(date_clone.getFullYear(), date_clone.getMonth())
                }
            }

            // For each user, work out if there's anything to do here.
            for (x in $scope.users) {
                user = $scope.users[x];

                if (user['dates'] === undefined) {
                    user['dates'] = []
                }

                // If there's a multiday event, next_date_check will be set, so we don't need to check for events.
                if (user['next_date_check'] !== undefined && user['next_date_check'].isAfter(date_clone)) {
                    continue;
                }

                items = $scope.timeline_items.filter(function(item) {
                    // Reduce the items down to only the current user.
                    current_user = item.user == user.id;

                    if (current_user === false) {
                        return false;
                    }

                    // Is the loop date within the item's date?
                    return date_clone.between(Date.parse(item.start_date), Date.parse(item.end_date))
                });

                if (items.length > 0) {
                    // Set the next_date_check.
                    user['next_date_check'] = Date.parse(items[0].end_date).addDays(1);
                }

                user['dates'].push({
                    'date': date_clone.toString('yyyy-MM-dd'),
                    'days': items.length > 0 ? items[0].days : 1,
                    'item': items.length > 0 ? items[0].project : false,
                });

                $scope.users[x] = user;
            };

            // Add a day to move the loop along.
            working_date.addDays(1);
        }

        // Reduce down the user dates.
        console.log($scope.users[0].dates);
        $scope.date_length = $scope.dates.length;
    });
});
