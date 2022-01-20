api_endpoint = window.location.origin + "/api/resolution/"

function create_view_button(id)
{
  var button = '<a href="#" class="btn btn-sm btn-success"\
                title="view" data-toggle="modal" data-target="#view-resolution' + id + '">' +
                '<i class="fa fa-eye"></i></a>';

  return button;
}

function create_edit_button(id)
{
  var button = '<a href="#" class="btn btn-sm btn-success"\
                title="view" data-toggle="modal" data-target="#edit-resolution' + id + '">' +
                '<i class="fa fa-edit"></i></a>';

  return button;
}

function create_delete_button(id)
{
  var button = '<a href="#" class="btn btn-sm btn-success"\
                title="view" data-toggle="modal" data-target="#delete-resolution' + id + '">' +
                '<i class="fa fa-trash"></i></a>';

  return button;
}

function add_new_resolution()
{
  var resolution = document.getElementById("resolution").value;
  var description = document.getElementById("description").value;
  var new_resolution = JSON.stringify({
    resolution: resolution,
    description: description
  })

  var request = new XMLHttpRequest();
  request.onreadystatechange = function () {
    if (this.readyState == 4) {
      var response = JSON.parse(this.responseText);
      if (this.status == 200){
        swal({
          icon: "success",
          text: response.message,
          title: "Success!",
        });
      } else {
        swal({
          icon: "error",
          text: response.message,
          title: "Error!"
        });
      }
    }
  }

  request.open("POST", api_endpoint, true);
  request.setRequestHeader("Content-Type", "application/json");
  request.send(new_resolution);

  document.getElementById("resolution").value = "";
  document.getElementById("description").value = "";
}
