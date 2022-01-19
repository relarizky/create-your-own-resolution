function create_view_button(id) {
  var button = '<a href="#" class="btn btn-sm btn-success"\
                title="view" data-toggle="modal" data-target="#view-resolution' + id + '">' +
                '<i class="fa fa-eye"></i></a>';

  return button;
}

function create_edit_button(id) {
  var button = '<a href="#" class="btn btn-sm btn-success"\
                title="view" data-toggle="modal" data-target="#edit-resolution' + id + '">' +
                '<i class="fa fa-edit"></i></a>';

  return button;
}

function create_delete_button(id) {
  var button = '<a href="#" class="btn btn-sm btn-success"\
                title="view" data-toggle="modal" data-target="#delete-resolution' + id + '">' +
                '<i class="fa fa-trash"></i></a>';

  return button;
}
