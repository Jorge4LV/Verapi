import React from "react";
import { Flex, Text, Button, Heading, Box } from "@chakra-ui/react"; // Usamos Chakra UI para estilos simples.

export default function Home() {
  const discordInviteLink = "https://discord.gg/tu-invite"; // Reemplaza con tu link de invitación.

  return (
    <Flex
      direction="column"
      alignItems="center"
      justifyContent="center"
      minHeight="100vh"
      backgroundColor="black"
      color="white"
      padding="4"
    >
      {/* Nombre del club */}
      <Heading as="h1" fontSize="6xl" fontWeight="bold" marginBottom="6">
        CLUB DUDUA
      </Heading>

      {/* Descripción */}
      <Text fontSize="xl" textAlign="center" maxWidth="600px" marginBottom="8">
        Somos un servidor de <strong>Roleplay en Discord</strong>. Ven a
        explorar historias, compartir fantasías y sumergirte en un mundo lleno
        de posibilidades.
      </Text>

      {/* Botón para unirse */}
      <Button
        size="lg"
        colorScheme="purple"
        onClick={() => window.open(discordInviteLink, "_blank")}
        marginBottom="8"
      >
        Unirse al Club
      </Button>

      {/* Información sobre el bot */}
      <Box
        backgroundColor="gray.700"
        padding="4"
        borderRadius="md"
        textAlign="center"
        maxWidth="500px"
      >
        <Text fontSize="md">
          Actualmente, el bot del club está alojado en nuestra URL del CDN.
        </Text>
        <Text fontSize="sm" color="gray.400">
          Pregunta en el servidor si tienes dudas o necesitas soporte técnico.
        </Text>
      </Box>
    </Flex>
  );
}