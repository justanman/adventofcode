defmodule Dive do
  def part1() do
    {pos, depth} = read_input()
    |> Enum.reduce({0, 0}, fn
      {"forward", units}, {pos, depth} -> {pos + units, depth}
      {"down", units}, {pos, depth} -> {pos, depth + units}
      {"up", units}, {pos, depth} -> {pos, depth - units}
    end)
    pos * depth
  end

  def part2() do
    {pos, depth, _aim} = read_input()
    |> Enum.reduce({0, 0, 0}, fn
      {"down", units}, {pos, depth, aim} -> {pos, depth, aim + units}
      {"up", units}, {pos, depth, aim} -> {pos, depth, aim - units}
      {"forward", units}, {pos, depth, aim} -> {pos + units, depth + (aim * units), aim}
    end)
    pos * depth
  end

  def read_input() do
    File.read!("input.txt")
    |> String.trim()
    |> String.split("\n")
    |> Enum.map(&String.split(&1, " "))
    |> Enum.map(fn [command, units] -> {command, String.to_integer(units)} end)
  end
end
