defmodule SonarSweep do
  def part1() do
    read_input()
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.count(fn [a, b] -> b > a end)
  end

  def part2() do
    read_input()
    |> Enum.chunk_every(3, 1, :discard)
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.count(fn [a, b] -> Enum.sum(b) > Enum.sum(a) end)
  end

  def read_input() do
    File.read!("input.txt")
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
  end
end
