#!/usr/bin/env ruby
require "atmosphere"

class Cloud
  TYPES = ["Cumulus", "Stratus", "Cirrus", "Nimbostratus"].freeze

  attr_accessor :color, :altitude
  attr_reader :type

  def initialize(color, type = nil)
    @color = color
    @type = type || TYPES.sample
    @altitude = gen_altitude
  end

  def climb(increase = nil)
    # One dark but not so stormy night...
    @altitude += increase if increase
    @altitude
  end

  private

  def gen_altitude
    rand(0..100)
  end
end
