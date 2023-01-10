require 'csv'

class Array
  def find_duplicates
    select.with_index do |e, i|
      i
      self.index(e)
      i != self.index(e)
    end
  end

  def slow_find_duplicates
    group_by { |e| e }.
      each_with_object([]) do |i, arr|
        arr << i.last.drop(1)
      end.flatten
  end
end


all = CSV.open('characters.tsv', col_sep: "\t")
data = all.read

data.shift # Remove header

new_data = data.map do |row|
  row.delete(nil)
  row.shift # Remove first item
  row
end

data2 = new_data.select { |row| row.size == 1 }
  .map { |row| row[0] }

data2.each { |row| puts row.inspect }

puts "Ohne Alternativen:"
puts data2.size
puts data2.uniq.size

puts "Duplikate ohne Alternativen:"
puts data2.find_duplicates.inspect
