import { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone", // Necesario para trabajar en Vercel con múltiples builds
};

export default nextConfig;