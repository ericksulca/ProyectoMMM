var español={
  "sProcessing":"Procesando...",
  "sLengthMenu":"Mostrar _MENU_ registros",
  "sZeroRecords":"No se encontraron resultados",
  "zEmptyTable":"Ningún dato disponible en esta sala",
  "sInfo":"Mostrando registros del _START_ al _END_ de _TOTAL_ registros",
  "sInfoEmpty":"Mostrando registros del 0 al 0 de un total de 0 registros",
  "sInfoFiltered":"(filtrando de un total de _MAX_ registros)",
  "sInfoPostFix":"",
  "sSearch":"Buscar...",
  "sUrl":"",
  "sInfoThousands":"Cargando...",
  "oPaginate":{
    "sFirst":"Primero",
    "sLast":"Último",
    "sNext":"Siguiente",
    "sPrevious":"Anterior"
  },
  "oAria":{
    "sSortAscending":": Activar para ordenar la columna de manera ascendente",
    "sSortDescending":": Activar para ordenar la columna de manera descendente"
  }
}

$(document).ready(function(){
  $('#dataTable').DataTable({
    "language":español
  });
  $('#dataTableModal').DataTable({
    "language":español
  });
  $('.dataTable').DataTable({
    "language":español
  });
}
)
