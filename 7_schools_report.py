"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"

East Carolina University
Southern Methodist University
Temple University
Tulane University of Louisiana
United States Naval Academy
University of Central Florida
University of Cincinnati-Main Campus
University of Houston
University of Memphis
University of South Florida

"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"

Baylor University
Iowa State University
Kansas State University
Oklahoma State University-Main Campus
Texas Christian University
Texas Tech University
The University of Texas at Austin
University of Kansas
University of Oklahoma-Norman Campus
West Virginia University


"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"

Indiana University-Bloomington
Michigan State University
Northwestern University
Ohio State University-Main Campus
Purdue University-Main Campus
Rutgers University-New Brunswick
The Pennsylvania State University
University of Illinois Urbana-Champaign
University of Iowa
University of Maryland-College Park
University of Michigan-Ann Arbor
University of Minnesota-Twin Cities
University of Nebraska-Lincoln
University of Wisconsin-Madison

"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"

Auburn University
Louisiana State University and Agricultural & Mechanical College
Mississippi State University
Texas A & M University-College Station
The University of Alabama
The University of Tennessee-Knoxville
University of Arkansas
University of Florida
University of Florida-Online
University of Georgia
University of Kentucky
University of Mississippi
University of Missouri-Columbia
University of South Carolina-Columbia
Vanderbilt University




Display report for all universities that have a graduation rate for Women over 50%

Abilene Christian University
Graduation rate for women: 67

Academy of Art University
Graduation rate for women: 53

Adelphi University
Graduation rate for women: 73

American University
Graduation rate for women: 81

Anderson University
Graduation rate for women: 60

Appalachian State University
Graduation rate for women: 76

Arizona State University Campus Immersion
Graduation rate for women: 69

Arkansas State University
Graduation rate for women: 59

Ashland University
Graduation rate for women: 68

Auburn University
Graduation rate for women: 83

Augusta University
Graduation rate for women: 51

Aurora University
Graduation rate for women: 66

Austin Peay State University
Graduation rate for women: 55

Azusa Pacific University
Graduation rate for women: 70

Ball State University
Graduation rate for women: 69

Baylor University
Graduation rate for women: 81

Belmont University
Graduation rate for women: 72

Bemidji State University
Graduation rate for women: 51

Bentley University
Graduation rate for women: 92

Binghamton University
Graduation rate for women: 86

Biola University
Graduation rate for women: 74

Bloomsburg University of Pennsylvania
Graduation rate for women: 62

Boise State University
Graduation rate for women: 59

Boston College
Graduation rate for women: 93

Boston University
Graduation rate for women: 89

Bowling Green State University-Main Campus
Graduation rate for women: 66

Bradley University
Graduation rate for women: 78

Brandeis University
Graduation rate for women: 91

Bridgewater State University
Graduation rate for women: 63

Brigham Young University-Hawaii
Graduation rate for women: 69

Brigham Young University-Idaho
Graduation rate for women: 60

Brigham Young University-Provo
Graduation rate for women: 79

Brown University
Graduation rate for women: 95

Bryant University
Graduation rate for women: 87

Bucknell University
Graduation rate for women: 89

Butler University
Graduation rate for women: 87

California Baptist University
Graduation rate for women: 65

California Polytechnic State University-San Luis Obispo
Graduation rate for women: 86

California State Polytechnic University-Pomona
Graduation rate for women: 73

California State University-Channel Islands
Graduation rate for women: 57

California State University-Chico
Graduation rate for women: 69

California State University-Dominguez Hills
Graduation rate for women: 53

California State University-Fresno
Graduation rate for women: 62

California State University-Fullerton
Graduation rate for women: 74

California State University-Long Beach
Graduation rate for women: 77

California State University-Los Angeles
Graduation rate for women: 57

California State University-Monterey Bay
Graduation rate for women: 61

California State University-Northridge
Graduation rate for women: 61

California State University-Sacramento
Graduation rate for women: 57

California State University-San Bernardino
Graduation rate for women: 63

California State University-San Marcos
Graduation rate for women: 61

California State University-Stanislaus
Graduation rate for women: 58

California University of Pennsylvania
Graduation rate for women: 53

Calvin University
Graduation rate for women: 78

Campbell University
Graduation rate for women: 59

Carnegie Mellon University
Graduation rate for women: 93

Case Western Reserve University
Graduation rate for women: 88

Cedarville University
Graduation rate for women: 75

Central Connecticut State University
Graduation rate for women: 57

Central Michigan University
Graduation rate for women: 68

Central Washington University
Graduation rate for women: 62

Chamberlain University-Illinois
Graduation rate for women: 58

Chapman University
Graduation rate for women: 82

Christopher Newport University
Graduation rate for women: 83

Clarion University of Pennsylvania
Graduation rate for women: 56

Clemson University
Graduation rate for women: 90

Cleveland State University
Graduation rate for women: 51

Coastal Carolina University
Graduation rate for women: 51

Colgate University
Graduation rate for women: 90

Colorado Christian University
Graduation rate for women: 63

Colorado School of Mines
Graduation rate for women: 88

Colorado State University-Fort Collins
Graduation rate for women: 71

Columbia University in the City of New York
Graduation rate for women: 96

Concordia University-Saint Paul
Graduation rate for women: 52

Concordia University-Wisconsin
Graduation rate for women: 66

Cornell University
Graduation rate for women: 96

Creighton University
Graduation rate for women: 85

Dartmouth College
Graduation rate for women: 96

Davenport University
Graduation rate for women: 57

Delaware State University
Graduation rate for women: 51

DePaul University
Graduation rate for women: 72

Drexel University
Graduation rate for women: 75

Duke University
Graduation rate for women: 97

Duquesne University
Graduation rate for women: 82

East Carolina University
Graduation rate for women: 70

East Stroudsburg University of Pennsylvania
Graduation rate for women: 59

East Tennessee State University
Graduation rate for women: 54

Eastern Connecticut State University
Graduation rate for women: 63

Eastern Illinois University
Graduation rate for women: 54

Eastern Washington University
Graduation rate for women: 54

Elon University
Graduation rate for women: 84

Embry-Riddle Aeronautical University-Daytona Beach
Graduation rate for women: 72

Emory University
Graduation rate for women: 93

Endicott College
Graduation rate for women: 80

Fairfield University
Graduation rate for women: 81

Fairleigh Dickinson University-Metropolitan Campus
Graduation rate for women: 53

Ferris State University
Graduation rate for women: 51

Fitchburg State University
Graduation rate for women: 61

Florida Agricultural and Mechanical University
Graduation rate for women: 63

Florida Atlantic University
Graduation rate for women: 59

Florida Gulf Coast University
Graduation rate for women: 57

Florida International University
Graduation rate for women: 73

Florida National University-Main Campus
Graduation rate for women: 52

Florida State University
Graduation rate for women: 86

Fordham University
Graduation rate for women: 83

Framingham State University
Graduation rate for women: 61

Frostburg State University
Graduation rate for women: 59

Gannon University
Graduation rate for women: 69

George Mason University
Graduation rate for women: 77

George Washington University
Graduation rate for women: 88

Georgetown University
Graduation rate for women: 94

Georgia College & State University
Graduation rate for women: 64

Georgia Institute of Technology-Main Campus
Graduation rate for women: 92

Georgia Southern University
Graduation rate for women: 60

Georgia State University
Graduation rate for women: 58

Gonzaga University
Graduation rate for women: 90

Grand Valley State University
Graduation rate for women: 72

Hampton University
Graduation rate for women: 61

Harding University
Graduation rate for women: 74

Harvard University
Graduation rate for women: 98

High Point University
Graduation rate for women: 71

Hofstra University
Graduation rate for women: 67

Hope College
Graduation rate for women: 80

Howard University
Graduation rate for women: 67

Illinois State University
Graduation rate for women: 74

Indiana University of Pennsylvania-Main Campus
Graduation rate for women: 59

Indiana University-Bloomington
Graduation rate for women: 82

Indiana University-East
Graduation rate for women: 51

Indiana University-Purdue University-Indianapolis
Graduation rate for women: 53

Inter American University of Puerto Rico-San German
Graduation rate for women: 51

Iowa State University
Graduation rate for women: 78

Ithaca College
Graduation rate for women: 80

Jacksonville State University
Graduation rate for women: 52

James Madison University
Graduation rate for women: 85

Johns Hopkins University
Graduation rate for women: 95

Johnson & Wales University-Providence
Graduation rate for women: 68

Kansas State University
Graduation rate for women: 72

Kean University
Graduation rate for women: 54

Keiser University-Ft Lauderdale
Graduation rate for women: 71

Kennesaw State University
Graduation rate for women: 52

Kent State University at Kent
Graduation rate for women: 67

Kutztown University of Pennsylvania
Graduation rate for women: 55

La Salle University
Graduation rate for women: 66

Lander University
Graduation rate for women: 53

Lee University
Graduation rate for women: 67

Lehigh University
Graduation rate for women: 93

Lewis University
Graduation rate for women: 71

Liberty University
Graduation rate for women: 56

Lindenwood University
Graduation rate for women: 54

Longwood University
Graduation rate for women: 71

Louisiana State University and Agricultural & Mechanical College
Graduation rate for women: 74

Louisiana Tech University
Graduation rate for women: 70

Loyola Marymount University
Graduation rate for women: 85

Loyola University Chicago
Graduation rate for women: 78

Loyola University Maryland
Graduation rate for women: 82

Loyola University New Orleans
Graduation rate for women: 58

Marist College
Graduation rate for women: 87

Marquette University
Graduation rate for women: 84

Marshall University
Graduation rate for women: 54

Maryville University of Saint Louis
Graduation rate for women: 77

Massachusetts Institute of Technology
Graduation rate for women: 97

MCPHS University
Graduation rate for women: 72

Mercer University
Graduation rate for women: 78

Merrimack College
Graduation rate for women: 76

Metropolitan State University
Graduation rate for women: 53

Miami University-Oxford
Graduation rate for women: 85

Michigan State University
Graduation rate for women: 84

Michigan Technological University
Graduation rate for women: 82

Middle Tennessee State University
Graduation rate for women: 55

Millersville University of Pennsylvania
Graduation rate for women: 56

Minnesota State University Moorhead
Graduation rate for women: 61

Minnesota State University-Mankato
Graduation rate for women: 56

Mississippi State University
Graduation rate for women: 68

Missouri State University-Springfield
Graduation rate for women: 61

Missouri University of Science and Technology
Graduation rate for women: 70

Monmouth University
Graduation rate for women: 75

Montana State University
Graduation rate for women: 65

Montclair State University
Graduation rate for women: 72

Morgan State University
Graduation rate for women: 53

Murray State University
Graduation rate for women: 56

New Mexico State University-Main Campus
Graduation rate for women: 55

New York University
Graduation rate for women: 89

Nicholls State University
Graduation rate for women: 51

North Carolina A & T State University
Graduation rate for women: 58

North Carolina Central University
Graduation rate for women: 53

North Carolina State University at Raleigh
Graduation rate for women: 88

North Dakota State University-Main Campus
Graduation rate for women: 65

Northeastern University
Graduation rate for women: 92

Northern Arizona University
Graduation rate for women: 59

Northern Illinois University
Graduation rate for women: 51

Northern Kentucky University
Graduation rate for women: 52

Northwest Missouri State University
Graduation rate for women: 58

Northwestern University
Graduation rate for women: 96

Norwich University
Graduation rate for women: 63

Nova Southeastern University
Graduation rate for women: 61

NUC University
Graduation rate for women: 67

Oakland University
Graduation rate for women: 60

Ohio State University-Main Campus
Graduation rate for women: 89

Ohio University-Main Campus
Graduation rate for women: 69

Oklahoma State University-Main Campus
Graduation rate for women: 68

Old Dominion University
Graduation rate for women: 57

Oral Roberts University
Graduation rate for women: 59

Oregon State University
Graduation rate for women: 72

Pace University
Graduation rate for women: 62

Pepperdine University
Graduation rate for women: 91

Pittsburg State University
Graduation rate for women: 57

Plymouth State University
Graduation rate for women: 61

Point Loma Nazarene University
Graduation rate for women: 76

Pontifical Catholic University of Puerto Rico-Ponce
Graduation rate for women: 52

Princeton University
Graduation rate for women: 99

Purdue University-Main Campus
Graduation rate for women: 85

Quinnipiac University
Graduation rate for women: 80

Radford University
Graduation rate for women: 60

Regent University
Graduation rate for women: 62

Regis University
Graduation rate for women: 70

Rensselaer Polytechnic Institute
Graduation rate for women: 90

Rice University
Graduation rate for women: 96

Rider University
Graduation rate for women: 66

Robert Morris University
Graduation rate for women: 76

Roger Williams University
Graduation rate for women: 73

Rowan University
Graduation rate for women: 72

Rutgers University-Camden
Graduation rate for women: 70

Rutgers University-New Brunswick
Graduation rate for women: 87

Rutgers University-Newark
Graduation rate for women: 68

Sacred Heart University
Graduation rate for women: 74

Saginaw Valley State University
Graduation rate for women: 53

Saint Edward's University
Graduation rate for women: 70

Saint Joseph's University
Graduation rate for women: 84

Saint Leo University
Graduation rate for women: 51

Saint Louis University
Graduation rate for women: 83

Saint Xavier University
Graduation rate for women: 55

Salem State University
Graduation rate for women: 61

Salisbury University
Graduation rate for women: 71

Sam Houston State University
Graduation rate for women: 61

Samford University
Graduation rate for women: 78

San Diego State University
Graduation rate for women: 79

San Francisco State University
Graduation rate for women: 60

San Jose State University
Graduation rate for women: 70

Santa Clara University
Graduation rate for women: 94

Seattle University
Graduation rate for women: 74

Seton Hall University
Graduation rate for women: 73

Shippensburg University of Pennsylvania
Graduation rate for women: 56

Slippery Rock University of Pennsylvania
Graduation rate for women: 71

Sonoma State University
Graduation rate for women: 64

South Dakota State University
Graduation rate for women: 63

Southeast Missouri State University
Graduation rate for women: 55

Southeastern University
Graduation rate for women: 52

Southern Connecticut State University
Graduation rate for women: 53

Southern Illinois University-Carbondale
Graduation rate for women: 51

Southern Illinois University-Edwardsville
Graduation rate for women: 57

Southern Methodist University
Graduation rate for women: 83

Southern Utah University
Graduation rate for women: 51

Southwest Minnesota State University
Graduation rate for women: 58

St. John's University-New York
Graduation rate for women: 67

Stanford University
Graduation rate for women: 96

State University of New York at New Paltz
Graduation rate for women: 77

Stephen F Austin State University
Graduation rate for women: 58

Stetson University
Graduation rate for women: 65

Stevens Institute of Technology
Graduation rate for women: 91

Stevenson University
Graduation rate for women: 65

Stockton University
Graduation rate for women: 77

Stony Brook University
Graduation rate for women: 81

Strayer University-Virginia
Graduation rate for women: 67

Suffolk University
Graduation rate for women: 62

SUNY at Albany
Graduation rate for women: 70

SUNY Brockport
Graduation rate for women: 69

SUNY College of Technology at Alfred
Graduation rate for women: 55

SUNY Cortland
Graduation rate for women: 73

Syracuse University
Graduation rate for women: 85

Temple University
Graduation rate for women: 78

Tennessee Technological University
Graduation rate for women: 61

Texas A & M International University
Graduation rate for women: 52

Texas A & M University-College Station
Graduation rate for women: 86

Texas A & M University-Commerce
Graduation rate for women: 51

Texas Christian University
Graduation rate for women: 85

Texas State University
Graduation rate for women: 59

Texas Tech University
Graduation rate for women: 65

The Catholic University of America
Graduation rate for women: 84

The College of New Jersey
Graduation rate for women: 90

The New School
Graduation rate for women: 73

The Pennsylvania State University
Graduation rate for women: 76

The University of Alabama
Graduation rate for women: 74

The University of Findlay
Graduation rate for women: 63

The University of Tampa
Graduation rate for women: 63

The University of Tennessee-Chattanooga
Graduation rate for women: 54

The University of Tennessee-Knoxville
Graduation rate for women: 75

The University of Tennessee-Martin
Graduation rate for women: 57

The University of Texas at Arlington
Graduation rate for women: 56

The University of Texas at Austin
Graduation rate for women: 90

The University of Texas at Dallas
Graduation rate for women: 75

The University of Texas at Tyler
Graduation rate for women: 52

The University of Texas Rio Grande Valley
Graduation rate for women: 54

The University of West Florida
Graduation rate for women: 53

Thomas Jefferson University
Graduation rate for women: 72

Towson University
Graduation rate for women: 75

Trine University
Graduation rate for women: 62

Troy University
Graduation rate for women: 53

Truman State University
Graduation rate for women: 78

Tufts University
Graduation rate for women: 95

Tulane University of Louisiana
Graduation rate for women: 87

United States Air Force Academy
Graduation rate for women: 88

United States Military Academy
Graduation rate for women: 83

United States Naval Academy
Graduation rate for women: 87

University at Buffalo
Graduation rate for women: 81

University of Alabama at Birmingham
Graduation rate for women: 65

University of Alabama in Huntsville
Graduation rate for women: 60

University of Arizona
Graduation rate for women: 69

University of Arkansas
Graduation rate for women: 72

University of California-Berkeley
Graduation rate for women: 94

University of California-Davis
Graduation rate for women: 88

University of California-Irvine
Graduation rate for women: 88

University of California-Los Angeles
Graduation rate for women: 93

University of California-Merced
Graduation rate for women: 72

University of California-Riverside
Graduation rate for women: 80

University of California-San Diego
Graduation rate for women: 89

University of California-Santa Barbara
Graduation rate for women: 85

University of California-Santa Cruz
Graduation rate for women: 79

University of Central Florida
Graduation rate for women: 79

University of Central Missouri
Graduation rate for women: 55

University of Chicago
Graduation rate for women: 96

University of Cincinnati-Main Campus
Graduation rate for women: 75

University of Colorado Boulder
Graduation rate for women: 77

University of Connecticut
Graduation rate for women: 86

University of Dayton
Graduation rate for women: 85

University of Delaware
Graduation rate for women: 86

University of Denver
Graduation rate for women: 78

University of Florida
Graduation rate for women: 91

University of Florida-Online
Graduation rate for women: 71

University of Georgia
Graduation rate for women: 90

University of Hartford
Graduation rate for women: 58

University of Hawaii at Manoa
Graduation rate for women: 63

University of Houston
Graduation rate for women: 67

University of Houston-Clear Lake
Graduation rate for women: 57

University of Idaho
Graduation rate for women: 65

University of Illinois Chicago
Graduation rate for women: 66

University of Illinois Urbana-Champaign
Graduation rate for women: 89

University of Indianapolis
Graduation rate for women: 63

University of Iowa
Graduation rate for women: 73

University of Kansas
Graduation rate for women: 66

University of Kentucky
Graduation rate for women: 70

University of La Verne
Graduation rate for women: 70

University of Louisiana at Lafayette
Graduation rate for women: 55

University of Louisiana at Monroe
Graduation rate for women: 57

University of Louisville
Graduation rate for women: 64

University of Maine
Graduation rate for women: 61

University of Mary Hardin-Baylor
Graduation rate for women: 58

University of Mary Washington
Graduation rate for women: 68

University of Maryland-Baltimore County
Graduation rate for women: 74

University of Maryland-College Park
Graduation rate for women: 89

University of Massachusetts-Amherst
Graduation rate for women: 85

University of Massachusetts-Boston
Graduation rate for women: 56

University of Massachusetts-Dartmouth
Graduation rate for women: 56

University of Massachusetts-Lowell
Graduation rate for women: 77

University of Memphis
Graduation rate for women: 56

University of Miami
Graduation rate for women: 84

University of Michigan-Ann Arbor
Graduation rate for women: 94

University of Michigan-Dearborn
Graduation rate for women: 59

University of Minnesota-Duluth
Graduation rate for women: 65

University of Minnesota-Twin Cities
Graduation rate for women: 86

University of Mississippi
Graduation rate for women: 69

University of Missouri-Columbia
Graduation rate for women: 78

University of Missouri-Kansas City
Graduation rate for women: 56

University of Missouri-St Louis
Graduation rate for women: 57

University of Nebraska at Kearney
Graduation rate for women: 64

University of Nebraska at Omaha
Graduation rate for women: 51

University of Nebraska-Lincoln
Graduation rate for women: 69

University of Nevada-Reno
Graduation rate for women: 63

University of New England
Graduation rate for women: 62

University of New Hampshire-Main Campus
Graduation rate for women: 78

University of New Haven
Graduation rate for women: 67

University of New Mexico-Main Campus
Graduation rate for women: 56

University of North Alabama
Graduation rate for women: 56

University of North Carolina at Asheville
Graduation rate for women: 65

University of North Carolina at Chapel Hill
Graduation rate for women: 92

University of North Carolina at Charlotte
Graduation rate for women: 68

University of North Carolina at Greensboro
Graduation rate for women: 62

University of North Carolina Wilmington
Graduation rate for women: 76

University of North Dakota
Graduation rate for women: 64

University of North Florida
Graduation rate for women: 70

University of North Texas
Graduation rate for women: 65

University of Northern Colorado
Graduation rate for women: 55

University of Northern Iowa
Graduation rate for women: 67

University of Northwestern-St Paul
Graduation rate for women: 78

University of Notre Dame
Graduation rate for women: 97

University of Oklahoma-Norman Campus
Graduation rate for women: 75

University of Oregon
Graduation rate for women: 77

University of Pennsylvania
Graduation rate for women: 96

University of Pittsburgh-Pittsburgh Campus
Graduation rate for women: 86

University of Portland
Graduation rate for women: 87

University of Puerto Rico-Arecibo
Graduation rate for women: 55

University of Puerto Rico-Humacao
Graduation rate for women: 56

University of Puerto Rico-Mayaguez
Graduation rate for women: 56

University of Puerto Rico-Rio Piedras
Graduation rate for women: 56

University of Rhode Island
Graduation rate for women: 74

University of Richmond
Graduation rate for women: 89

University of Rochester
Graduation rate for women: 87

University of San Diego
Graduation rate for women: 81

University of San Francisco
Graduation rate for women: 73

University of Scranton
Graduation rate for women: 84

University of South Alabama
Graduation rate for women: 52

University of South Carolina-Columbia
Graduation rate for women: 81

University of South Carolina-Upstate
Graduation rate for women: 51

University of South Dakota
Graduation rate for women: 62

University of South Florida
Graduation rate for women: 78

University of Southern California
Graduation rate for women: 93

University of Southern Indiana
Graduation rate for women: 56

University of Southern Mississippi
Graduation rate for women: 53

University of St Thomas
Graduation rate for women: 82

University of the Incarnate Word
Graduation rate for women: 59

University of the Pacific
Graduation rate for women: 77

University of Toledo
Graduation rate for women: 57

University of Utah
Graduation rate for women: 70

University of Vermont
Graduation rate for women: 81

University of Virginia-Main Campus
Graduation rate for women: 95

University of Washington-Bothell Campus
Graduation rate for women: 66

University of Washington-Seattle Campus
Graduation rate for women: 86

University of Washington-Tacoma Campus
Graduation rate for women: 61

University of Wisconsin-Eau Claire
Graduation rate for women: 64

University of Wisconsin-Green Bay
Graduation rate for women: 58

University of Wisconsin-La Crosse
Graduation rate for women: 72

University of Wisconsin-Madison
Graduation rate for women: 91

University of Wisconsin-Oshkosh
Graduation rate for women: 59

University of Wisconsin-Platteville
Graduation rate for women: 58

University of Wisconsin-River Falls
Graduation rate for women: 59

University of Wisconsin-Stevens Point
Graduation rate for women: 62

University of Wisconsin-Stout
Graduation rate for women: 66

University of Wisconsin-Whitewater
Graduation rate for women: 67

University of Wyoming
Graduation rate for women: 64

Utah State University
Graduation rate for women: 56

Utica College
Graduation rate for women: 66

Vanderbilt University
Graduation rate for women: 94

Villanova University
Graduation rate for women: 93

Virginia Commonwealth University
Graduation rate for women: 70

Virginia Polytechnic Institute and State University
Graduation rate for women: 90

Wake Forest University
Graduation rate for women: 91

Washburn University
Graduation rate for women: 55

Washington State University
Graduation rate for women: 63

Washington University in St Louis
Graduation rate for women: 96

Wayne State College
Graduation rate for women: 56

Wayne State University
Graduation rate for women: 54

West Chester University of Pennsylvania
Graduation rate for women: 78

West Texas A & M University
Graduation rate for women: 52

West Virginia University
Graduation rate for women: 67

Western Carolina University
Graduation rate for women: 68

Western Connecticut State University
Graduation rate for women: 55

Western Governors University
Graduation rate for women: 56

Western Kentucky University
Graduation rate for women: 58

Western Michigan University
Graduation rate for women: 61

Western Washington University
Graduation rate for women: 70

Westfield State University
Graduation rate for women: 63

Wichita State University
Graduation rate for women: 54

William & Mary
Graduation rate for women: 94

William Carey University
Graduation rate for women: 58

William Paterson University of New Jersey
Graduation rate for women: 62

Winona State University
Graduation rate for women: 63

Winston-Salem State University
Graduation rate for women: 54

Winthrop University
Graduation rate for women: 62

Worcester Polytechnic Institute
Graduation rate for women: 92

Worcester State University
Graduation rate for women: 62

Xavier University
Graduation rate for women: 71

Yale University
Graduation rate for women: 97


Display report for all universities that have a total price for in-state students living off campus over $50,000

Abilene Christian University
Total price for in-state students living off campus: $53,672.00

Adelphi University
Total price for in-state students living off campus: $63,285.00

American University
Total price for in-state students living off campus: $69,299.00

Azusa Pacific University
Total price for in-state students living off campus: $63,812.00

Barry University
Total price for in-state students living off campus: $51,574.00

Baylor University
Total price for in-state students living off campus: $66,750.00

Belmont University
Total price for in-state students living off campus: $56,450.00

Bentley University
Total price for in-state students living off campus: $73,985.00

Biola University
Total price for in-state students living off campus: $59,758.00

Boston College
Total price for in-state students living off campus: $74,902.00

Boston University
Total price for in-state students living off campus: $77,662.00

Bradley University
Total price for in-state students living off campus: $50,200.00

Brandeis University
Total price for in-state students living off campus: $72,615.00

Bryant University
Total price for in-state students living off campus: $61,763.00

Bucknell University
Total price for in-state students living off campus: $75,922.00

Butler University
Total price for in-state students living off campus: $61,830.00

California Baptist University
Total price for in-state students living off campus: $58,722.00

Calvin University
Total price for in-state students living off campus: $52,606.00

Campbell University
Total price for in-state students living off campus: $54,331.00

Carnegie Mellon University
Total price for in-state students living off campus: $75,950.00

Case Western Reserve University
Total price for in-state students living off campus: $72,128.00

Chapman University
Total price for in-state students living off campus: $75,814.00

Columbia University in the City of New York
Total price for in-state students living off campus: $86,704.00

Cornell University
Total price for in-state students living off campus: $78,632.00

Creighton University
Total price for in-state students living off campus: $58,618.00

DePaul University
Total price for in-state students living off campus: $59,793.00

Drexel University
Total price for in-state students living off campus: $76,400.00

Duquesne University
Total price for in-state students living off campus: $59,104.00

Elon University
Total price for in-state students living off campus: $54,562.00

Embry-Riddle Aeronautical University-Daytona Beach
Total price for in-state students living off campus: $56,596.00

Emory University
Total price for in-state students living off campus: $72,884.00

Endicott College
Total price for in-state students living off campus: $51,096.00

Fairfield University
Total price for in-state students living off campus: $69,230.00

Fairleigh Dickinson University-Metropolitan Campus
Total price for in-state students living off campus: $60,654.00

Fordham University
Total price for in-state students living off campus: $72,559.00

Gannon University
Total price for in-state students living off campus: $52,561.00

George Washington University
Total price for in-state students living off campus: $76,276.00

Gonzaga University
Total price for in-state students living off campus: $64,802.00

Hawaii Pacific University
Total price for in-state students living off campus: $52,020.00

High Point University
Total price for in-state students living off campus: $54,080.00

Hofstra University
Total price for in-state students living off campus: $74,335.00

Ithaca College
Total price for in-state students living off campus: $65,527.00

Johns Hopkins University
Total price for in-state students living off campus: $69,392.00

Lehigh University
Total price for in-state students living off campus: $72,065.00

Long Island University
Total price for in-state students living off campus: $68,636.00

Loyola Marymount University
Total price for in-state students living off campus: $75,279.00

Loyola University Chicago
Total price for in-state students living off campus: $60,668.00

Loyola University Maryland
Total price for in-state students living off campus: $62,050.00

Loyola University New Orleans
Total price for in-state students living off campus: $60,194.00

Marist College
Total price for in-state students living off campus: $61,045.00

Marquette University
Total price for in-state students living off campus: $64,978.00

Massachusetts Institute of Technology
Total price for in-state students living off campus: $64,462.00

MCPHS University
Total price for in-state students living off campus: $57,042.00

Mercer University
Total price for in-state students living off campus: $54,856.00

Merrimack College
Total price for in-state students living off campus: $63,931.00

Monmouth University
Total price for in-state students living off campus: $55,430.00

New York University
Total price for in-state students living off campus: $77,632.00

Northeastern University
Total price for in-state students living off campus: $75,732.00

Northwestern University
Total price for in-state students living off campus: $81,283.00

Norwich University
Total price for in-state students living off campus: $62,004.00

Nova Southeastern University
Total price for in-state students living off campus: $55,602.00

Pace University
Total price for in-state students living off campus: $72,326.00

Pepperdine University
Total price for in-state students living off campus: $77,912.00

Point Loma Nazarene University
Total price for in-state students living off campus: $60,602.00

Quinnipiac University
Total price for in-state students living off campus: $68,980.00

Regis University
Total price for in-state students living off campus: $56,300.00

Rice University
Total price for in-state students living off campus: $69,557.00

Rider University
Total price for in-state students living off campus: $55,960.00

Roger Williams University
Total price for in-state students living off campus: $54,038.00

Sacred Heart University
Total price for in-state students living off campus: $59,162.00

Saint Edward's University
Total price for in-state students living off campus: $66,374.00

Saint Joseph's University
Total price for in-state students living off campus: $65,606.00

Saint Louis University
Total price for in-state students living off campus: $64,892.00

Samford University
Total price for in-state students living off campus: $51,900.00

Santa Clara University
Total price for in-state students living off campus: $75,300.00

Seattle University
Total price for in-state students living off campus: $65,970.00

Seton Hall University
Total price for in-state students living off campus: $65,358.00

Southern Methodist University
Total price for in-state students living off campus: $70,640.00

St. John's University-New York
Total price for in-state students living off campus: $60,785.00

St. Thomas University
Total price for in-state students living off campus: $54,819.00

Stetson University
Total price for in-state students living off campus: $68,240.00

Stevens Institute of Technology
Total price for in-state students living off campus: $74,462.00

Stevenson University
Total price for in-state students living off campus: $51,168.00

Suffolk University
Total price for in-state students living off campus: $65,433.00

Syracuse University
Total price for in-state students living off campus: $75,652.00

Texas Christian University
Total price for in-state students living off campus: $71,828.00

The Catholic University of America
Total price for in-state students living off campus: $69,386.00

The New School
Total price for in-state students living off campus: $69,176.00

Thomas Jefferson University
Total price for in-state students living off campus: $62,052.00

Tufts University
Total price for in-state students living off campus: $79,000.00

Tulane University of Louisiana
Total price for in-state students living off campus: $78,680.00

University of Dayton
Total price for in-state students living off campus: $62,220.00

University of Denver
Total price for in-state students living off campus: $70,414.00

University of Hartford
Total price for in-state students living off campus: $59,888.00

University of La Verne
Total price for in-state students living off campus: $68,222.00

University of Miami
Total price for in-state students living off campus: $77,432.00

University of New England
Total price for in-state students living off campus: $53,500.00

University of New Haven
Total price for in-state students living off campus: $58,180.00

University of Notre Dame
Total price for in-state students living off campus: $76,883.00

University of Pennsylvania
Total price for in-state students living off campus: $78,828.00

University of Portland
Total price for in-state students living off campus: $62,316.00

University of Richmond
Total price for in-state students living off campus: $72,450.00

University of San Diego
Total price for in-state students living off campus: $75,166.00

University of San Francisco
Total price for in-state students living off campus: $73,872.00

University of Scranton
Total price for in-state students living off campus: $60,456.00

University of Southern California
Total price for in-state students living off campus: $80,151.00

University of St Thomas
Total price for in-state students living off campus: $65,282.00

University of the Incarnate Word
Total price for in-state students living off campus: $50,905.00

University of the Pacific
Total price for in-state students living off campus: $73,396.00

Villanova University
Total price for in-state students living off campus: $75,835.00

Wake Forest University
Total price for in-state students living off campus: $77,278.00

Washington University in St Louis
Total price for in-state students living off campus: $79,586.00

Worcester Polytechnic Institute
Total price for in-state students living off campus: $72,296.00

Xavier University
Total price for in-state students living off campus: $60,270.00

"""
