class RowsToDict:

    def row_to_dict(self, row):
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))

        return d

    def generate_list(self, result_query):
        result = []
        for row in result_query:
            result.append(self.row_to_dict(row))

        return result
