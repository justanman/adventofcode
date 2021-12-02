defmodule SonarSweep do
  def part1() do
    File.read!("input.txt")
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.filter(fn [a, b] -> b > a end)
    |> Enum.count()
  end

  def part2() do
    File.read!("input.txt")
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
    |> Enum.chunk_every(3, 1, :discard)
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.filter(fn [a, b] -> Enum.sum(b) > Enum.sum(a) end)
    |> Enum.count()
  end
end
