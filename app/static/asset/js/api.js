api_endpoint = window.location.origin + "/api/resolution/"

function create_view_button(data)
{
  var button = '<a href="#" class="btn btn-sm btn-success"\
                title="view" data-toggle="modal" data-target="#view-resolution' + data.id + '">' +
                '<i class="fa fa-eye"></i></a>';
  var modal = '<div class="modal fade bd-example-modal-lg" id="view-resolution' + data.id + '" tabindex="-1" role="dialog" aria-labelledby="add-resolution-modal" aria-hidden="true">\
                              <div class="modal-dialog modal-dialog-centered modal-lg" role="document">\
                                <div class="modal-content">\
                                  <div class="modal-header">\
                                    <h5 class="modal-title" id="add-resolution-title">\
                                      Your Resolution\
                                    </h5>\
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">\
                          <span aria-hidden="true">&times;</span>\
                        </button>\
                      </div>\
                      <div class="modal-body">\
                        <form>\
                          <div class="form-group">\
                            <label for="resolution">Resolution :</label>\
                            <input type="text" name="resolution" class="form-control" aria-describedby="your-resolution" value="' + data.resolution + '" disabled>\
                          </div>\
                          <div class="form-group">\
                            <label for="description-or-notes">Description / Notes :</label>\
                            <textarea class="form-control" name="description" rows="5" disabled>' + data.description + '</textarea>\
                          </div>\
                        </form>\
                      </div>\
                      <div class="modal-footer">\
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>\
                        <!--<button type="button" class="btn btn-primary">Submit</button>-->\
                      </div>\
                    </div>\
                  </div>\
                </div>';

  return button + modal;
}

function create_edit_button(data)
{
  var button = '<a href="#" class="btn btn-sm btn-warning"\
                title="edit" data-toggle="modal" data-target="#edit-resolution' + data.id + '">' +
                '<i class="fa fa-edit"></i></a>';
  var modal = '<div class="modal fade bd-example-modal-lg" id="edit-resolution'+data.id+'" tabindex="-1" role="dialog" aria-labelledby="add-new-modal" aria-hidden="true">\
    <div class="modal-dialog modal-dialog-centered modal-lg" role="document">\
      <div class="modal-content">\
        <div class="modal-header">\
          <h5 class="modal-title" id="add-new-title">\
            Edit Resolution\
          </h5>\
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">\
            <span aria-hidden="true">&times;</span>\
          </button>\
        </div>\
        <div class="modal-body">\
          <form>\
            <div class="form-group">\
              <label for="resolution">Resolution :</label>\
              <input type="text" id="resolution'+data.id+'" name="resolution'+data.id+'" class="form-control" aria-describedby="your-resolution" value="'+data.resolution+'" placeholder="your resolution">\
            </div>\
            <div class="form-group">\
              <label for="description-or-notes">Description / Notes :</label>\
              <textarea class="form-control" id="description'+data.id+'" name="description'+data.id+'" rows="5" placeholder="your description / notes">'+data.description+'</textarea>\
            </div>\
            <div class="form-group">\
              <label for="percentage">Percentage Of Your Progress :</label>\
              <input type="text" id="number'+data.id+'" class="form-control" value="'+data.percentage+'%" disabled>\
              <input type="range" id="percentage'+data.id+'" class="form-control" name="percentage'+data.id+'" value='+data.percentage+' min=0 max=100 step=1>\
            </div>\
          </form>\
        </div>\
        <div class="modal-footer">\
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>\
          <button type="button" class="btn btn-primary" onclick="edit_resolution('+data.id+')">Submit</button>\
        </div>\
      </div>\
    </div>\
  </div>\
  <script type="text/javascript">\
  $("#percentage'+data.id+'").on("input change", function (){\
          $("#number'+data.id+'").val($("#percentage'+data.id+'").val().concat("%"));\
        });\
  </script>';
  return button + modal;
}

function create_delete_button(data)
{
  var button = '<a href="#" class="btn btn-sm btn-danger"\
                title="delete" data-toggle="modal" data-target="#delete-resolution' + data.id + '">' +
                '<i class="fa fa-trash"></i></a>';
  var modal = '<div class="modal fade" id="delete-resolution'+data.id+'" tabindex="-1" role="dialog" aria-labelledby="add-new-modal" aria-hidden="true">\
    <div class="modal-dialog modal-dialog-centered" role="document">\
      <div class="modal-content">\
        <div class="modal-header">\
          <h5 class="modal-title" id="delete-resolution-title">\
            Delete this resolution?\
          </h5>\
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">\
            <span aria-hidden="true">&times;</span>\
          </button>\
        </div>\
        <div class="modal-body">\
          <p>Are you sure you want to delete this resolution?</p>\
        </div>\
        <div class="modal-footer">\
          <button type="button" class="btn btn-danger" onclick="delete_resolution('+data.id+')">Delete</button>\
        </div>\
      </div>\
    </div>\
  </div>';

  return button + modal;
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
  $("#resolution-table").DataTable().ajax.reload();
}

function delete_resolution(id)
{
  var endpoint = api_endpoint + id
  var request = new XMLHttpRequest()

  request.onreadystatechange = function() {
    if (this.readyState == 4){
      var response = JSON.parse(this.responseText);
      if (this.status == 200){
        swal({
          icon: "success",
          text: response.message,
          title: "Success!"
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

  request.open("DELETE", endpoint, true);
  request.send();
  $("#delete-resolution" + id).modal('hide');
  $("#resolution-table").DataTable().ajax.reload();
}

function edit_resolution(id)
{
  var endpoint = api_endpoint + id;
  var resolution = document.getElementById('resolution'+id).value;
  var percentage = document.getElementById('percentage'+id).value;
  var description = document.getElementById('description'+id).value;
  var resolution_json = JSON.stringify({
    'resolution': resolution,
    'percentage': percentage,
    'description': description
  });

  var request = new XMLHttpRequest();
  request.onreadystatechange = function(){
    if (this.readyState == 4){
      var response = JSON.parse(this.responseText);
      if (this.status == 200){
        swal({
          icon: "success",
          text: response.message,
          title: "Success!"
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

  request.open("PUT", endpoint, true);
  request.setRequestHeader("Content-Type", "application/json");
  request.send(resolution_json);
  $("#edit-resolution" + id).modal('hide');
  $("#resolution-table").DataTable().ajax.reload();
}
