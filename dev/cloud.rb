#!/usr/bin/env ruby
require 'atmosphere'

class Cloud
  TYPES = ['Cumulus', 'Stratus', 'Cirrus', 'Nimbostratus'].freeze

  attr_accessor :color, :altitude
  attr_reader :type

  def initialize(color, type = nil)
    # One dark but not so stormy night...
    @color = color
    @type = type || TYPES.sample
    @altitude = gen_altitude
  end

  def climb(increase = nil)
    @altitude += increase if increase
    @altitude
  end

  private

  def gen_altitude
    rand(100..1000)
  end
end

my_cloud = Cloud.new('gray')
print "New cloud: #{my_cloud}\n"
