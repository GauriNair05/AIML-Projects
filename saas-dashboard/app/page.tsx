"use client";

import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import { LayoutDashboard, Users, CreditCard, Settings, Activity } from "lucide-react";

const chartData = [
  { month: "Jan", revenue: 4000 },
  { month: "Feb", revenue: 3000 },
  { month: "Mar", revenue: 5000 },
  { month: "Apr", revenue: 8000 },
  { month: "May", revenue: 6000 },
  { month: "Jun", revenue: 9500 },
];

export default function Dashboard() {
  return (
    <div className="flex h-screen bg-gray-900 text-white font-sans">
      <aside className="w-64 bg-gray-800 p-6 border-r border-gray-700 flex flex-col justify-between">
        <div>
          <h1 className="text-xl font-bold mb-8 flex items-center gap-2 text-indigo-400">
            <Activity /> SaaS Cloud
          </h1>
          <nav className="space-y-4">
            <a href="#" className="flex items-center gap-3 text-indigo-400 font-medium">
              <LayoutDashboard size={20} /> Dashboard
            </a>
            <a href="#" className="flex items-center gap-3 text-gray-400 hover:text-white">
              <Users size={20} /> Customers
            </a>
            <a href="#" className="flex items-center gap-3 text-gray-400 hover:text-white">
              <CreditCard size={20} /> Billing
            </a>
            <a href="#" className="flex items-center gap-3 text-gray-400 hover:text-white">
              <Settings size={20} /> Settings
            </a>
          </nav>
        </div>
      </aside>

      <main className="flex-1 p-8 overflow-y-auto">
        <header className="mb-8">
          <h2 className="text-3xl font-semibold">Overview</h2>
          <p className="text-gray-400 text-sm">Real-time metrics and system state.</p>
        </header>

        <section className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-gray-800 p-6 rounded-xl border border-gray-700">
            <p className="text-gray-400 text-sm">Total Revenue</p>
            <h3 className="text-3xl font-bold mt-2">$35,500</h3>
          </div>
          <div className="bg-gray-800 p-6 rounded-xl border border-gray-700">
            <p className="text-gray-400 text-sm">Active Users</p>
            <h3 className="text-3xl font-bold mt-2">1,240</h3>
          </div>
          <div className="bg-gray-800 p-6 rounded-xl border border-gray-700">
            <p className="text-gray-400 text-sm">Churn Rate</p>
            <h3 className="text-3xl font-bold mt-2">1.2%</h3>
          </div>
        </section>

        <section className="bg-gray-800 p-6 rounded-xl border border-gray-700">
          <h3 className="text-lg font-medium mb-6">Revenue Growth</h3>
          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData}>
                <XAxis dataKey="month" stroke="#9CA3AF" />
                <YAxis stroke="#9CA3AF" />
                <Tooltip contentStyle={{ backgroundColor: "#1F2937", border: "none" }} />
                <Bar dataKey="revenue" fill="#6366F1" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </section>
      </main>
    </div>
  );
}