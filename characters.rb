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

characters = data.each_with_index.map do |row, index|
  row.delete(nil)

  id = index + 1
  keyword = row.shift
  translations = row

  Character.new(id, keyword, translations)
end

all_translations = characters.inject([]) { |arr, c| arr << c.translations }
all_translations.flatten!
puts all_translations.inspect
puts all_translations.size

# Select characters with only one translation.
characters_w_one_translation = characters.select { |character| character.translations.size == 1 }

#characters_w_one_translation.each { |character| puts character.inspect }
puts characters_w_one_translation.size

chars_uniq_translations = characters_w_one_translation.select { |c| all_translations.count(c.translations[0]) == 1 }
chars_uniq_translations.each { |c| puts c }
puts chars_uniq_translations.size
