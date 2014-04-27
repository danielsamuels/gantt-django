var ganttApp = angular.module('ganttApp', [])

ganttApp.controller('DataCtrl', function($scope, $http) {

    $http.get('/data/').success(function(data) {

        for (item in data) {
            $scope[item] = data[item];
        }

        // Generate a full date range.
        $scope.dates = []
        $scope.months = {}

        working_date = Date.parse(data.start_date);
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

            // Add a day to move the loop along.
            working_date.addDays(1);
        }

        $scope.date_length = $scope.dates.length;
    });
});
