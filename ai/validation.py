class ModelValidation:

    def should_activate(

        self,

        old_wr,

        new_wr,

        old_pf,

        new_pf

    ):

        if new_wr < old_wr:
            return False

        if new_pf < old_pf:
            return False

        return True