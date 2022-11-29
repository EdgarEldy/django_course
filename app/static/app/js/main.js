// Get products by category_id using ajax

$(function () {
  $("#category_id").on("change", function () {
    category_id = $(this).val();
    // alert(category_id);
    $.get(
      "/orders/getProducts",
      {
        category_id: category_id,
      },
      function (data) {
        $("#id_product").html(data);
      }
    );
  });
});

// Get unit_price by id_product
$(function () {
  $("#id_product").on("change", function () {
    id_product = $(this).val();
    // alert(id_product);
    $.get(
      "/orders/getUnitPrice",
      {
        id_product: id_product,
      },
      function (data) {
        $("#unit_price").val(data);
      }
    );
  });
});

$('#id_qty').on('keyup', function () {
  var id_qty = $(this).val();
  // alert(id_qty)
  var unit_price = $('#unit_price').val();
  var total = id_qty * unit_price;
  $('#id_total').val(total);
});