var conferre = angular.module('conferre', []);

conferre.controller('VentaSillasCtrl', function($http, $scope) {

$scope.conferencias = [];
$scope.sillas = []
$scope.fecha = new Date();

$scope.precio = $scope.silla.precio;

$http.get('/obtener_conferencias', {
      params: {}
    }).then(function(response){
    return response.data.conferencias.map(function(item){
        $scope.conferencias.append(item);
      });
    });

    $http.get('/obtener_sillas', {
      params: {}
    }).then(function(response){
    return response.data.sillas.map(function(item){
        $scope.sillas.append(item);
      });
    });

$scope.registrar_venta = function(val) {
    return $http.get('/registrar_venta', {
      params: {
        cantidad: $scope.cantidad,
        conferencia: $scope.conferencia,
        silla: $scope.silla,
        fecha: $scope.fecha.getDate()
      }
    }).then(function(response){
            $scope.message = response
      });
    });
  };


});
