defmodule BinaryDiagnostic do
  def part1() do
    input = read_input()
    counts = input
    |> Enum.reduce([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], fn bit_list, acc ->
      for x <- 0..11 do
        Enum.at(bit_list, x) + Enum.at(acc, x)
      end
    end)

    gamma_rate = counts
    |> Enum.map(fn count ->
      if count < (length(input) / 2), do: 0, else: 1
    end) |> Enum.join() |> String.to_integer(2)

    epsilon_rate = counts
    |> Enum.map(fn count ->
      if count > (length(input) / 2), do: 0, else: 1
    end) |> Enum.join() |> String.to_integer(2)

    gamma_rate * epsilon_rate
  end

  def part2() do

  end

  def read_input() do
    File.read!("input.txt")
    |> String.split("\n", trim: true)
    |> Enum.map(fn string -> string |> String.graphemes() |> Enum.map(fn bit -> String.to_integer(bit) end) end)
  end
end
