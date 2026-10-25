require 'yaml'
root = File.expand_path('..', __dir__)
paths = Dir[File.join(root, '.agents/skills/*/SKILL.md')].sort
raise 'Expected 20 Skills' unless paths.size == 20
paths.each do |path|
  match = File.read(path).match(/\A---\n(.*?)\n---\n/m)
  raise "Missing frontmatter: #{path}" unless match
  data = YAML.safe_load(match[1])
  name = File.basename(File.dirname(path))
  raise "Invalid name: #{path}" unless data['name'] == name && name.match?(/\A[a-z0-9]+(?:-[a-z0-9]+)*\z/) && name.length < 64
  raise "Invalid description: #{path}" unless data['description'].is_a?(String) && data['description'].length.between?(1, 1024)
end
puts 'PASS: 20 YAML frontmatters (Ruby Psych safe_load)'
