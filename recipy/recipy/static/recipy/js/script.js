const addMoreBtn = document.getElementById("add-more");
const totalNewForms = document.getElementById("id_ingredients-TOTAL_FORMS");

addMoreBtn.addEventListener("click", addNewForm);

function addNewForm(event) {
  if (event) {
    event.preventDefault();
  }
  const currentIngredientForms = document.getElementsByClassName("ingredient-form");
  let currentFormCount = currentIngredientForms.length; //+ 1
  const formCopyTarget = document.getElementById("ingredient-form-list");
  const copyEmptyFormEl = document.getElementById("empty-form").cloneNode(true);
  copyEmptyFormEl.setAttribute("class", "ingredient-form");
  copyEmptyFormEl.setAttribute("id", `form=${currentFormCount}`);
  const regex = new RegExp("__prefix__", "g");
  totalNewForms.setAttribute("value", currentFormCount + 1);
  copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount);
  formCopyTarget.append(copyEmptyFormEl);
}
