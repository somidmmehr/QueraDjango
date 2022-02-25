// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
    var toastLiveExample = document.getElementById('liveToast')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        $(form).find("input").removeClass("is-invalid")
        $(form).addClass('was-validated')

        if (!form.checkValidity()) {
          event.stopPropagation()
          return null;
        }
        console.log("1")
        $.ajax({
            url: "",
            type: "post",
            data: $("#rform").serialize(),
            dataType: 'json',
            success: function(Response){
                console.log("2")
                console.log(Response)
                /*
                if(Response.result){
                    window.location.href = "/home";
                    return false;
                }
                $(form).find("input").addClass("is-valid")
                $(form).removeClass('was-validated')
                var toast = new bootstrap.Toast($("#liveToast"))
                toast.show()
                $("#liveToast").find(".toast-body").text(Response.errors[0])
                $("#"+Response.errors[1]+"").addClass("is-invalid")
                $("#"+Response.errors[1]+"").siblings(".invalid-feedback").text(Response.errors[0])
                console.log(Response.errors)
                */
            }
        })
      }, false)
    })
})()
