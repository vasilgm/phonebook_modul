import text
import view
import model

def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                if result:
                    index = view.ID_change_cont()
                    name = view.name_change_cont()
                    phone = view.phone_change_cont()
                    comment = view.comment_change_cont()
                    model.change(index, name, phone, comment)
                    view.print_message(text.change_successful)
            case 7:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                if result:
                    index = view.ID_del_cont()
                    model.remove(index)
                    view.print_message(text.del_successful)


            case 8:
                view.print_message(text.exit_program)
                break
