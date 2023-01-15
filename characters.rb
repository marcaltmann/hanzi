require 'csv'

class Array
  def find_duplicates
    select.with_index do |e, i|
      i
      self.index(e)
      i != self.index(e)
    end
  end
end


all = CSV.open('characters.tsv', col_sep: "\t")
data = all.read

data.shift # Remove header

Character = Data.define(:id, :keyword, :translations)

new_data = data.each_with_index.map do |row, index|
  row.delete(nil)

  id = index + 1
  keyword = row.shift
  translations = row

  Character.new(id, keyword, translations)
end

# Select characters with only one translation.
data2 = new_data.select { |character| character.translations.size == 1 }

data2.each { |character| puts character.inspect }
puts data2.size
