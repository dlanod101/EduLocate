from django.shortcuts import render
import folium
from folium import plugins
from folium.plugins import MarkerCluster
import branca

# Create your views here.
def index(request):
    m = folium.Map(location=[4.9757, 8.3417], zoom_start=12, tiles="OpenStreetMap")

    # Add the full screen button.                                               
    plugins.Fullscreen(                                                         
        position                = "topright",                                   
        title                   = "Open full-screen map",                       
        title_cancel            = "Close full-screen map",                      
        force_separate_button   = True,                                         
    ).add_to(map_) 

    # List of schools with their coordinates and popup info
    schools = [
        {"name": "Calabar Preparatory International School", "coords": [4.954901863249359, 8.337468672558513], "info": "This institution is a well-regarded school that provides a solid foundation in early education with a focus on preparatory and primary school levels. It is known for its quality curriculum aimed at equipping young learners with academic and life skills in a nurturing environment."},
        {"name": "UNICAL International Demonstration Secondary School", "coords": [4.95644104031808, 8.34622340221119], "info": "Located within the University of Calabar, UCIDSS offers a unique blend of academic excellence and a focus on developing the “total child.” With a motto of “Excellence, Strength, and Service,” the school emphasizes academic achievement, moral values, and extracurricular engagement to prepare students for the challenges of life and leadership. It has a strong reputation in both academics and competitions"},
        {"name": "Nuevas Fronteras First School", "coords": [4.968754327686409, 8.335237074803908], "info": "This is a private institution offering early childhood education and primary-level learning, with a focus on international standards and a commitment to shaping global-minded students."},
        {"name": "Kings and Queens Schools", "coords": [4.955072883100703, 8.333520461146518], "info": "Known for its comprehensive academic offerings, this school focuses on both primary and secondary education. It seeks to foster leadership, discipline, and academic rigor in a modern, supportive learning environment."},
        {"name": "Holy Child Secondary School", "coords": [4.959348364996844, 8.329057265637312], "info": "**Holy Child Secondary School** in Calabar, Cross River State, is a prominent Catholic institution known for its commitment to academic excellence and moral teachings. The school offers a rigorous curriculum that prepares students for external examinations like WASSCE and UTME, while also promoting discipline and character development. With a range of extracurricular activities, Holy Child fosters well-rounded personal growth, emphasizing leadership skills and ethical values. It is recognized for shaping students into responsible individuals ready to face future challenges."},
        {"name": "Springfield High School", "coords": [4.952507580684402, 8.330430556563224], "info": "A secondary school that provides a well-rounded education, combining academic work with extracurricular activities to prepare students for higher education and professional life."},
        {"name": "Bluebells Schools (Nursery & Primary)", "coords": [4.971490582546004, 8.349656629525967], "info": "This school specializes in nursery and primary education, focusing on the early development of children. It offers a nurturing environment that encourages creativity and academic growth from a young age."},
        {"name": "Kourklys International School", "coords": [4.984658649965691, 8.341245222604766], "info": "Offering a blend of local and international curricula, this school focuses on developing academic excellence and global citizenship among its students."},
        {"name": "Aunty Margaret International School", "coords": [4.9730297209096905, 8.338326979387206], "info": " Aunty Margaret International School, located at 44/46 Ndedem Usang Iso Road in Calabar, was established in 2010 as a private institution. The school operates as a limited liability company, under the name Auntie Margaret International Memorial School Ltd. It is known for offering quality education within the Calabar municipality."},
        {"name": "Amethystfield Schools", "coords": [4.949087161981516, 8.326997329248446], "info": "This is a modern school that offers comprehensive educational services from early years to secondary level, focusing on academic achievement and character development."},
        {"name": "Salvation Army primary school", "coords": [4.953191662302111, 8.334722090706691], "info": "Salvation Army Primary School in Calabar is located on Goldie Street, Esin Ufot Efut. It serves as a public primary school in the area, focusing on providing foundational education to young students. In recent times, the school has benefited from community outreach programs, such as one by Sweetest Kiddies Empire, which provided students with much-needed school supplies like textbooks, sandals, and bags to aid in their education"},
        {"name": "Chilion International School", "coords": [4.932497880656623, 8.316011001841163], "info": "Chilion International School, located at Ikot Enebong, 8 Miles in Calabar, is known for providing a blend of British and Nigerian curricula, offering a rich academic environment. The school emphasizes learning through discipline and hard work, aiming to develop both innate and acquired abilities in its students. It has modern facilities like a standard ICT center, a multipurpose hall, and a sports complex. Extra-curricular activities include music, drama, and language classes, as well as clubs for arts and crafts, debate, and JETS (Junior Engineers, Technicians, and Scientists)"},
        
        {"name": "University of Calabar", "coords": [4.952776839979816, 8.33992759941126], "info": "The University of Calabar (UNICAL) tells a story of academic innovation and impact both in Nigeria and internationally. Established in 1975 as one of the country’s second-generation federal universities, UNICAL was originally a campus of the University of Nigeria before becoming independent. Known for its progressive approach, it was one of the first Nigerian universities to automate student registration and alumni relations, pioneering online transcript requests.<br><br>Designed by architect John Elliott, the campus stands as a symbol of UNICAL’s motto, 'Knowledge for Service'. The university’s library, also established in 1975, has grown into one of the largest in Nigeria, supporting the academic and research needs of students and faculty alike.<br><br>UNICAL’s comprehensive range of faculties, from Medicine and Engineering to Environmental Sciences and Law, fosters interdisciplinary learning. Its commitment to education has produced notable alumni such as Godswill Akpabio, Senate President of Nigeria; Dr. Betta Edu, a leading public health specialist; Chile Eboe-Osuji, former President of the International Criminal Court; and Iyanya, a famous Nigerian singer.<br><br>These distinguished graduates highlight UNICAL’s role in shaping leaders and change-makers across various sectors, making it a powerhouse of academic excellence and societal contribution both in Nigeria and around the world."},

        {"name": "University of Cross River", "coords": [4.9292303588989625, 8.329933524016974], "info": "The University of Cross River State (UNICROSS), formerly known as the Cross River University of Technology (CRUTECH), is a state-owned institution with a deep historical connection to the region. In February 2021, a significant transformation occurred when the university's name was changed through a bill passed by the Cross River State House of Assembly. The move was aimed at expanding its academic offerings beyond technology-focused courses to a broader array of professional programs, marking its shift from a specialized technical institution to a conventional university.<br><br>UNICROSS traces part of its legacy back to the University of Cross River State, Uyo, which was established by Cross River State in 1983. However, when Akwa Ibom State was carved out from Cross River State in 1987, the institution was rebranded as the University of Uyo, transferring students, staff, and facilities to this new federal university in 1991.<br><br>In its modern form, UNICROSS was established in 2002 by merging three institutions: the Polytechnic of Calabar, the College of Education, and the Ibrahim Babangida College of Agriculture. This integration created a multi-disciplinary university with campuses in Calabar, Obubra, Ogoja, and Okuku, each serving as a hub for different academic faculties.<br><br>The university's faculties range from Biological Sciences and Engineering to Agriculture and Forestry, offering a wide variety of undergraduate and postgraduate programs. With departments such as Civil Engineering, Mass Communication, and Medical Biochemistry, UNICROSS has evolved into a diverse academic institution, serving students across Cross River State and beyond.<br><br>Located in Calabar South, the main campus houses key administrative offices, including that of the Vice-Chancellor, currently Prof. Augustine Angba. Through its multi-campus system, UNICROSS continues to contribute significantly to education in southern Nigeria, offering diverse opportunities for academic growth and professional development."},

        {"name": "Arthur Jarvis University", "coords": [4.939520196904116, 8.455605036990292], "info": "Arthur Jarvis University (AJU) in Akpabuyo, Cross River State, has quickly made its mark in Nigeria’s educational landscape as a private university dedicated to offering diverse and impactful programs. Established with a focus on providing quality education across multiple disciplines, AJU began its journey by welcoming 120 students at its first matriculation ceremony, signaling the start of its role in shaping future leaders.<br><br>AJU’s faculties cater to a wide range of interests and industries. From the Faculty of Natural and Applied Sciences, which offers programs like Geology, Microbiology, and Computer Science, to the Faculty of Humanities, Management, and Social Sciences, with studies in Criminology, Political Science, and Business Administration, the university encourages interdisciplinary learning. The Faculty of Basic Medical Sciences supports Nigeria’s health sector with courses such as Nursing Science, Public Health, and Optometry, while the Faculty of Law prepares students for the legal profession. The Faculty of Education is dedicated to shaping future educators in subjects ranging from Early Childhood Education to Vocational and Technical Education.<br>Despite being relatively young, AJU has already celebrated significant milestones. In April 2023, the university convocated 251 students at its combined convocation ceremony, showcasing its steady growth and success in fulfilling its educational mission. AJU’s admissions process ensures students come prepared to meet the rigorous academic standards, with requirements that include passing relevant exams like the JAMB UTME and achieving a minimum of five credits in secondary school exams.<br><br>AJU’s journey reflects the promise of a university that is not only expanding its academic offerings but also shaping the next generation of professionals and leaders in Nigeria. The story of Arthur Jarvis University is one of growth, commitment to quality education, and the pursuit of excellence across multiple fields."},

        {"name": "Hope Waddell Training Institution", "coords": [4.9745614888274545, 8.326300677472183], "info":"The Hope Waddell Training Institution (HOWAD), founded in 1895 by missionaries from the United Presbyterian Church of Scotland, is one of Nigeria’s most historically significant educational institutions. Named after Reverend Hope Masterton Waddell, it has long been a beacon of knowledge and innovation in Calabar, Cross River State. While the idea of founding such an institute faced initial reluctance, Scottish missionary Mary Mitchell Slessor's persistence paid off, leading to the creation of an institution modeled after two others in Africa, Lovedale Institute in South Africa and Livingstonia in Nyasaland.<br><br>The school’s early years were marked by a pioneering approach to vocational education. It offered practical training in fields such as carpentry, masonry, blacksmithing, and naval engineering. Female students were not left out, learning dressmaking, domestic science, and accounting. HOWAD quickly earned a reputation as West Africa's largest vocational school. A maritime vessel, ’The Diamond,’ was maintained by students for hands-on training in maritime subjects, and agriculture students introduced new crops to the region.<br><br>Interestingly, in 1902, soccer was introduced into the curriculum by Rev. James Luke, despite parental objections. Luke’s influence helped spread the love for soccer throughout Nigeria, and many graduates who moved to Lagos helped establish the sport in the country’s capital.<br><br>In addition to practical training, the school was pivotal in fostering intellectual development. Its print works produced Calabar's first newspaper, ’The Observer,’ and it provided comprehensive secondary education, earning recognition as a secondary examination center for the prestigious Cambridge Local Examination.<br><br>Although the institution faced decline after Nigeria’s independence in 1960, the Old Boys Association began rehabilitating the school in 1994. By 2005, major restoration projects were completed, including the renovation of science labs and the erection of a statue of Hope Waddell.<br><br>Notable alumni include Nigeria's first president, Dr. Nnamdi Azikiwe, former University of Lagos vice-chancellor Eni Njoku, and political leaders like Kingsley O. Mbadiwe and Dennis Osadebay. HOWAD’s legacy lives on through its contributions to Nigeria’s educational and socio-political fabric."}
        
    ]

    # Create a marker cluster
    marker_cluster = MarkerCluster().add_to(m)

    
    # Loop through each school and add its marker with a popup
    for school in schools:
        html = f"""
        <style>
            h1{{
                text-align: center;
            }}
        </style>
        <div>
            <h1>{school['name']}</h1>
            <p>{school['info']}</p>
        </div>
        """
        iframe = branca.element.IFrame(html=html, width=600, height=200)
        popup = folium.Popup(iframe, max_width=600)
        folium.Marker(
            location=school['coords'],
            tooltip='Click for more info',
            popup=popup,
            icon=folium.Icon('blue', 'white', icon='fas fa-university', prefix='fa')
        ).add_to(marker_cluster)

    # Render map in HTML
    m = m._repr_html_()
    context = {'m': m}
    return render(request, 'index.html', context)
