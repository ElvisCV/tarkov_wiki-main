# populate_weapons.py
# Script para poblar la base de datos con armas de prueba
# GUARDA ESTE ARCHIVO EN LA RAIZ DEL PROYECTO (junto a manage.py)

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tarkov_project.settings')
django.setup()

from weapons.models import Weapon

# Datos de armas de Escape from Tarkov
weapons_data = [
    {
        "name": "AK-74M",
        "description": "Rifle de asalto ruso calibre 5.45x39mm. Arma versatil con buen alcance y precision. Popular entre PMCs y Scavs por su disponibilidad y rendimiento.",
        "img": "https://images.unsplash.com/photo-1595590424283-b8f17842773f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "M4A1",
        "description": "Rifle de asalto estadounidense calibre 5.56x45mm NATO. Altamente personalizable con cientos de modificaciones disponibles. Excelente ergonomia y precision.",
        "img": "https://images.unsplash.com/photo-1614680376593-902f74cf0d41?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "Mosin Nagant",
        "description": "Rifle de cerrojo ruso calibre 7.62x54mmR. Arma economica con gran poder de penetracion. Ideal para francotiradores con presupuesto limitado.",
        "img": "https://images.unsplash.com/photo-1562804698-76c8cafc750c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "ADAR 2-15",
        "description": "Version civil del AR-15 calibre 5.56x45mm. Solo disparo semi-automatico pero altamente modificable. Buena opcion para iniciar en el meta del AR.",
        "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "MP5",
        "description": "Subfusil aleman calibre 9x19mm. Excelente control de retroceso y cadencia de fuego. Perfecto para combate en espacios cerrados.",
        "img": "https://images.unsplash.com/photo-1614680376408-81e91ffe3db7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "SKS",
        "description": "Rifle semi-automatico ruso calibre 7.62x39mm. Confiable y preciso a media distancia. Popular para Scavs por su bajo costo.",
        "img": "https://images.unsplash.com/photo-1595590424283-b8f17842773f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "DVL-10",
        "description": "Rifle de francotirador de precision calibre .308 Win. Extremadamente silencioso y preciso. Favorito de francotiradores sigilosos.",
        "img": "https://images.unsplash.com/photo-1562804698-76c8cafc750c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "SA-58",
        "description": "Rifle de batalla belga calibre 7.62x51mm NATO. Alto dano y penetracion a costa de mayor retroceso. Muy efectivo contra armadura pesada.",
        "img": "https://images.unsplash.com/photo-1614680376593-902f74cf0d41?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "MP7A2",
        "description": "PDW aleman calibre 4.6x30mm. Alta cadencia de fuego y municion perforante. Compacto y letal en manos expertas.",
        "img": "https://images.unsplash.com/photo-1614680376408-81e91ffe3db7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "RSASS",
        "description": "Rifle de tirador designado calibre 7.62x51mm NATO. Semi-automatico con excelente precision. Ideal para combate a larga distancia.",
        "img": "https://images.unsplash.com/photo-1562804698-76c8cafc750c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "P90",
        "description": "PDW belga calibre 5.7x28mm. Diseno bullpup unico con cargador de 50 balas. Excelente movilidad y capacidad de fuego.",
        "img": "https://images.unsplash.com/photo-1595590424283-b8f17842773f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "Glock 17",
        "description": "Pistola austriaca calibre 9x19mm. Confiable y economica. Buen arma secundaria o para raids de bajo presupuesto.",
        "img": "https://images.unsplash.com/photo-1614680376593-902f74cf0d41?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "AS VAL",
        "description": "Rifle de asalto ruso integrado con supresor calibre 9x39mm. Silencioso y letal. Municion subsonica con alta penetracion.",
        "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "HK416",
        "description": "Rifle de asalto aleman calibre 5.56x45mm. Version mejorada del M4 con mayor confiabilidad. Premium en todos los aspectos.",
        "img": "https://images.unsplash.com/photo-1614680376408-81e91ffe3db7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "VSS Vintorez",
        "description": "Rifle de francotirador silencioso ruso calibre 9x39mm. Hermano del AS VAL con optica integrada. Mortal en manos expertas.",
        "img": "https://images.unsplash.com/photo-1562804698-76c8cafc750c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "TOZ-106",
        "description": "Escopeta rusa calibre 20x70. Arma basica de Scav. Economica pero limitada en combate contra PMCs equipados.",
        "img": "https://images.unsplash.com/photo-1595590424283-b8f17842773f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "M1A",
        "description": "Rifle semi-automatico estadounidense calibre 7.62x51mm NATO. Preciso y potente. Version civil del M14.",
        "img": "https://images.unsplash.com/photo-1614680376593-902f74cf0d41?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "AKM",
        "description": "Rifle de asalto ruso calibre 7.62x39mm. Version modernizada del AK-47. Robusto y confiable con gran poder de detencion.",
        "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "SV-98",
        "description": "Rifle de francotirador ruso calibre 7.62x54mmR. Precision de nivel militar a precio accesible. Excelente para aprender francotirador.",
        "img": "https://images.unsplash.com/photo-1562804698-76c8cafc750c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "MPX",
        "description": "Subfusil estadounidense calibre 9x19mm. Modular y suave de disparar. Perfecto para CQB en mapas como Factory.",
        "img": "https://images.unsplash.com/photo-1614680376408-81e91ffe3db7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    },
]

def populate():
    print("Iniciando poblacion de armas...")
    print("-" * 50)
    
    # Limpiar armas existentes (opcional)
    # Weapon.objects.all().delete()
    # print("Armas existentes eliminadas.")
    
    created_count = 0
    updated_count = 0
    
    for weapon_data in weapons_data:
        weapon, created = Weapon.objects.get_or_create(
            name=weapon_data["name"],
            defaults={
                "description": weapon_data["description"]
                # Las imágenes se pueden subir manualmente desde el admin
            }
        )
        
        if created:
            created_count += 1
            print(f"[OK] Creada: {weapon.name}")
        else:
            updated_count += 1
            print(f"[EXISTS] Ya existia: {weapon.name}")
    
    print("-" * 50)
    print(f"Proceso completado:")
    print(f"- Armas creadas: {created_count}")
    print(f"- Armas que ya existian: {updated_count}")
    print(f"- Total en base de datos: {Weapon.objects.count()}")
    print("-" * 50)
    print("Puedes ver las armas en: http://127.0.0.1:8000/weapons/")
    print("O administrarlas en: http://127.0.0.1:8000/admin/")
    print("NOTA: Las imágenes se pueden subir manualmente desde el panel de administración")

if __name__ == "__main__":
    populate()