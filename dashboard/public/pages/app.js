   var myApp = angular.module('postgreSQL',['angularUtils.directives.dirPagination']);
            myApp.controller('postgreSQLCtrl', ['$scope' ,'$http',  function($scope,$http) {
                $scope.myVal = false;
                $scope.myVal2 = false;
                $scope.myVal3= false;
                $scope.getAllRec = function(){
                     $http({method: 'GET', url: '/db/readRecords'}).
                        success(function(data, status) {
                              $scope.dataset = data;
//                         console.log($scope.dataset);

                        }).
                        error(function(data, status) {
                          $scope.dataset = data || "Request failed";
                      });
                }
                $scope.getAllRec();

                $scope.femRec = function(){
                     $http({method: 'GET', url: '/db/femRec'}).
                        success(function(data, status) {
                              $scope.femDataset = data;
                        console.log($scope.femDataset);

                        }).
                        error(function(data, status) {
                          $scope.femDataset = data || "Request failed";
                      });
                }
                $scope.femRec();

                $scope.etaRec = function(){
                     $http({method: 'GET', url: '/db/etaRec'}).
                        success(function(data, status) {
                              $scope.etaDataset = data;
                        console.log($scope.etaDataset);

                        }).
                        error(function(data, status) {
                          $scope.etaDataset = data || "Request failed";
                      });
                }
                $scope.etaRec();


                $scope.clicked = function(row){
                    $scope.myVal = true;
                    $scope.myVal2= true;
                    var imo = row.imo2;

                    $http.post('/imo', {'imo':imo}).
                    success(function(data){
//                        console.log(imo);
                    }).error(function(data){
                             console.log("no data")
                             })

                    $scope.crewRec = function(){
                            $http({method: 'GET', url: '/db/peopleRec/'+imo}).
                        success(function(data, status) {
                              $scope.dataset2 = data;
                         console.log($scope.dataset2);

                        }).
                        error(function(data, status) {
                          $scope.dataset2 = data || "Request failed";
                      });
                }
                $scope.crewRec();

                //  $scope.weaponsRec = function(){
                //             $http({method: 'GET', url: '/db/weaponsRec/'+imo}).
                //         success(function(data, status) {
                //               $scope.dataset3 = data;
                //          console.log($scope.dataset3);
                //
                //         }).
                //         error(function(data, status) {
                //           $scope.dataset3 = data || "Request failed";
                //       });
                // }
                // $scope.weaponsRec();


                };
                $scope.clicked2 = function(row){
                    $scope.myVal2 = false;
                    $scope.myVal3= true;
                    var tdn = row.travel_document_number;

                    $http.post('/person', {'tdn':tdn}).
                    success(function(data){
                      // console.log(tdn)
                    }).error(function(data){
                             console.log("no data");
                             })

                    $scope.person = function(){
                            $http({method: 'GET', url: '/db/person/'+tdn}).
                        success(function(data, status) {
                              $scope.dataset4 = data;
                         console.log(data.Birth_Date);
                        }).
                        error(function(data, status) {
                          $scope.dataset4 = data || "Request failed";
                      });
                }
                $scope.person();

                };


            }]);
