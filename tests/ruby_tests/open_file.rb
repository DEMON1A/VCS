puts 'Enter file path:'
path = gets.chomp
puts 'File contents:'
open(path, 'r') do |file|
  until file.eof? do
    puts file.gets
  end
end
