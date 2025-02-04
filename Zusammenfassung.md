# 1.Modelling
## 1.1 Differentialgleichung
<p>Zunächst werden die Differentialgleichungen, die das dynamische Verhalten des Systems beschreiben, basierend auf den mechanischen Eigenschaften des Systems und physikalischen Gesetzen (wie den Newtonschen Gesetzen) aufgestellt. Diese Gleichungen sind in der Regel nichtlineare Differentialgleichungen höherer Ordnung.</p>

![1](Pic/001.PNG)
<p>Kräftegleichgewicht in X-Richtung für die Laufkatze:</p>

$
F_m = m_k \ddot{x}(t) + S \sin(v)
$

$F_m$ ist die Antriebskraft, die der Motor der Laufkatze bereitstellt.

$S$ ist die Kraft im Seil.

Kräftegleichgewicht des Gewichtsblocks in X- und Y-Richtung:

$
S \cos(v) = m_y \ddot{y_y} + m_y g
$

$
S \sin(v) = m_y \ddot{x_y}
$

Die Beziehung der Verschiebung der Laufkatze und des Gewichtsblocks in X- und Y-Richtung:

$
{x}(t) = {x_y}(t) + l(t) \sin(v)
$

$
{y_y}(t) = l(t) - l(t) \cos(v)
$

Um $F_m$ und $S$ auszugleichen, haben wir folgende Schritte durchgeführt:

$
\sin(v)(m_y \ddot{y_y} + m_y g) = \cos(v) m_y \ddot{x_y}
$

$
{x_y}(t) = {x}(t) - l(t) \sin(v)
$

Um die Modellierung zu vereinfachen, bleibt die Länge des Seils konstant.

$
\dot{x_y}(t) = \dot{x}(t) - \dot{l}(t) \sin(v) - l(t) \cos(v) \dot{v} ; \dot{l}(t) = 0 \quad \ddot{l}(t) = 0
$

$
\ddot{x_y}(t) = \ddot{x}(t) - l(t) (- \sin(v) \dot{v}^2 + \cos(v) \ddot{v})
$

$
{y_y}(t) = l(t) - l(t) \cos(v)
$

$
\dot{y_y}(t) = \dot{l}(t) - \dot{l}(t) \cos(v) - l(t) (-\sin(v) \dot{v}) ; \dot{l}(t) = 0 \quad \ddot{l}(t) = 0
$

$
\ddot{y_y}(t) = l(t) (\cos(v) \dot{v}^2 + \sin(v) \ddot{v})
$

$
\sin(v){m_y}l(t)(\cos(v)\dot{v}^2+\sin(v)\ddot{v})+\sin(v){m_y}g = \cos(v){m_y}(\ddot{x}(t)+l(t)\sin(v)\dot(v)^2-l(t)\cos(v)\ddot(v))
$

Schließlich erhalten wir eine nichtlineare Differentialgleichung:

$
l(t)\ddot{v}+\sin(v)g = \cos(v)\ddot{x}(t)
$

## 1.2 Linearisierung

<p>Da nichtlineare Differentialgleichungen nur schwer direkt analysiert werden können, muss das System in der Regel linearisiert werden. Die Linearisierung erfolgt in der Nähe eines bestimmten Arbeitspunkts des Systems, wobei die nichtlinearen Gleichungen durch lineare Gleichungen approximiert werden. Eine gängige Methode ist die Taylor-Entwicklung, bei der höhere Ordnungsglieder vernachlässigt werden, um die linearisierten Differentialgleichungen zu erhalten.</p>

Der Schwingwinkel des Seils ist in der Regel nicht sehr groß, daher können die trigonometrischen Funktionen angenähert werden.

$
\sin(x) \approx x
$

$
\cos(x) \approx 1
$

Dann können wir die linearisierten gewöhnlichen Differentialgleichungen erhalten:

$
l\ddot{v}+gv = \ddot{x}
$

## 1.3 Aufstellung der Zustandsgleichung

Zustandsvariablen sind die kleinste Menge von Variablen, die das dynamische Verhalten eines Systems vollständig beschreiben können. Die Wahl der Zustandsvariablen sollte sicherstellen, dass das dynamische Verhalten des Systems durch diese Variablen vollständig erfasst wird.

Nach der Linearisierung wird die Differentialgleichung in die Zustandsraumdarstellung umgewandelt. Die Zustandsraumdarstellung umfasst in der Regel die Zustandsgleichung und die Ausgangsgleichung:  

- **Zustandsgleichung**:  
  $\dot{x}(t) = A x(t) + B u(t)$ 

- **Ausgangsgleichung**:  
  $y(t) = C x(t) + D u(t)$ 

Wir wählen diese drei Variablen als Zustandsvariablen:

$x_1=lv-x$ 

$x_2=l\dot{v}-\dot{x}$

$x_3=x$ 

Zwischen der Eingabe 
$u$ und der Geschwindigkeit der Laufkatze besteht eine lineare Beziehung

$
\dot{\underline{x}} = \begin{bmatrix} 
0 & 1 & 0 \\ 
-g/l & 0 & -g/l \\ 
0 & 0 & 0 
\end{bmatrix}x+\begin{bmatrix} 
0  \\ 
0\\ 
c 
\end{bmatrix}u
$

Die Daten, die wir messen können, sind die relative Position der Laufkatze und der Winkel des Winkelsensors.
Daher lautet die Ausgangsgleichung:

$y = \begin{bmatrix} 
0 & 0 & c_2 \\ 
1/l & 0 & 1/l
\end{bmatrix}x$

Nach der Messung haben wir folgende Daten erhalten:

$l = 0.7m$

$c = 1.96$

$c_2 = 1/2.7 m^{-1}$

Als nächstes wird die Kontrollierbarkeit und Beobachtbarkeit des Modells überprüft.

Durch die Berechnung des Rangs der Steuerbarkeitsmatrix kann bestimmt werden, ob das System steuerbar ist. Wenn der Rang der Matrix der Anzahl der Zustandsvariablen entspricht, ist das System steuerbar, was bedeutet, dass der Zustand des Systems durch die Steuerungseingabe von jedem Anfangszustand in jeden anderen Zustand überführt werden kann.

$\underline{Q_s} = \begin{bmatrix} 
\underline{B} & \underline{A}\underline{B} & \underline{A^2}\underline{B} 
\end{bmatrix} =\begin{bmatrix} 
0 & 0 & -gc/l \\ 
0 & -gc/l & 0 \\ 
c & 0 & 0 
\end{bmatrix}$

$rank(\underline{Q_s}) = 3$

Deshalb ist das System steuerbar.

Durch die Berechnung des Rangs der Beobachtbarkeitsmatrix kann bestimmt werden, ob das System beobachtbar ist. Wenn der Rang der Matrix der Anzahl der Zustandsvariablen entspricht, ist das System beobachtbar, was bedeutet, dass der Zustand des Systems vollständig aus den Ausgangssignalen des Systems abgeleitet werden kann.

$\underline{Q_B} = \begin{bmatrix} 
\underline{C}\\ \underline{C}\underline{A}\\ \underline{C}\underline{A^2} 
\end{bmatrix}$

$rank(Q_B) = 3$

Deshalb ist das System beobachtbar.

## 1.4 Die Modellierung des Motors
Das Motormodell kann mit einem ersten Ordnung linearen Modell simuliert werden.

$M(s) = \frac{1}{1+0.2s}$

![](Pic/002.PNG)

Das Motormodell und das Zustandsraum-Modell bilden zusammen das Verladebrücke-Modell.

![](Pic/003.PNG)

# 2. H-Unendliche Regelung

Die softconstraints der H∞-Regelung sind Robustheit. Die Robustheit der H∞-Steuerung ergibt sich daraus, dass ihr Designkonzept speziell darauf ausgerichtet ist, die Leistung des Systems im Umgang mit Modellunsicherheiten und externen Störungen zu optimieren. Der Kerngedanke der H∞-Steuerung besteht darin, den schlimmsten Gewinn des Systems unter allen möglichen Störungen zu minimieren, um sicherzustellen, dass das System auch unter verschiedenen Unsicherheiten und Störungen stabil und leistungsfähig bleibt.

## 2.1 Unsicherheitsmodell

Die Motormodell ist nicht unbedingt eine PT-1-Struktur, und der Verstärkungsfaktor des Motormodells ist nicht unbedingt 1. Daher wird ein achtdimensionales SISO-Modell als Unsicherheit im Motormodell gewählt.

$M_{uns}(s) =M(s)*(1+W_{uns}*Uns)$

Die Sprungantwort des unsicheren Motormodells ist wie in der Abbildung dargestellt:

![](Pic/004.PNG)

## 2.2 Die Wahl der Gewichtungsmatrix

Wir möchten, dass das Ausgangssignal dem Referenzsignal folgt. Dies erfordert, dass der Betrag der geschlossenen Übertragungsfunktion eins ist.

$\frac{|G(iw)K(iw)|}{|1+G(iw)K(iw)|}\approx1$

Je kleiner der Wert der Sensitivitätsmatrix $|S(iw)|$ ist, desto besser ist die Verfolgsleistung.

$|S(iw)| = \frac{1}{|1+G(iw)K(iw)|}$

Bei niedrigen Frequenzen ist die Verfolgsleistung notwendig. Bei hohen Frequenzen besteht das System größtenteils aus Rauschen, sodass die Verfolgsleistung nicht erforderlich ist, da sie dem hochfrequenten Rauschen folgen würde. Daher wird eine Gewichtungsmatrix benötigt, um den Optimierungsbereich einzuschränken.$||W_p(iw)S(iw)||_{\infty}<1$; Die Gewichtungsmatrix ist in der Regel ein Tiefpassfilter.

Die Bode-Diagramme der beiden Tiefpassfilter sind im folgenden Bild dargestellt:

![](Pic/005.PNG)

![](Pic/006.PNG)

Diese beiden Gewichtungsübertragungsfunktionen müssen stabil sein, und die Sprungantworten dieser beiden Gewichtungsübertragungsfunktionen sind im folgenden Bild dargestellt:

![](Pic/007.PNG)

![](Pic/008.PNG)

## 2.3 H-Unendlich-Reglerdesign

Nach der Auswahl der Gewichtungsmatrix wird die Funktion ncfsyn in MATLAB zur Gestaltung des H-Unendlich-Reglers verwendet.

Die Simulationsergebnisse sind im folgenden Bild dargestellt:

Das Bild zeigt die Bewegung der Laufkatze von der Position 0 zur Position 0,9. Aus dem Bild ist ersichtlich, dass kein Überschwingen vorhanden ist und der Wagen nicht gegen den Rand stößt.

![](Pic/009.PNG)

Der Winkel der Seilschwingung nimmt allmählich ab.

![](Pic/010.PNG)

Das folgende Bild zeigt den Eingabewert u.

![](Pic/011.PNG)

# 3. Modellprädiktive Regelung (MPC)

Die Softconstraints der modellprädiktiven Regelung sind die Prädiktionsfunktion. Wir prädizieren die Position der Laufkatze, um eine Kollision der Laufkatze mit den Grenzen zu vermeiden.

## 3.1 Diskretisierung des Modells

Der Kern von MPC (Model Predictive Control) besteht darin, das zukünftige Verhalten des Systems mithilfe eines Modells vorherzusagen. Nach der Diskretisierung kann der Vorhersageprozess auf diskreten Zeitpunkten durchgeführt werden, was die Rechenkomplexität vereinfacht und gleichzeitig die Vorhersagegenauigkeit erhöht. Das diskretisierte Modell kann in ein lineares oder nichtlineares Optimierungsproblem umgewandelt werden. Diese Probleme sind standardisierte Optimierungsprobleme, für die es bereits effiziente Algorithmen (wie QP, SQP) gibt, um sie schnell zu lösen. Kontinuierliche Zeitmodelle erfordern möglicherweise die Behandlung komplexer Integral- oder Differentialoperationen, während diskretisierte Modelle durch einfache algebraische Operationen ersetzt werden können, was die Rechenlast erheblich reduziert und die Echtzeitanforderungen der Regelung erfüllt.

Wir diskretisieren das System mittels Nullstellenhalter-Methode.

Die Nullstellenhalter-Methode nimmt an, dass die Eingabe $u(t)$ während der Abtastperiode $T_s$ konstant bleibt, d.h.:

$
u(t) = u_k \quad \text{für} \quad t \in [kT_s, (k+1)T_s)
$

Basierend darauf kann die Lösung der Zustandsgleichung wie folgt dargestellt werden:

$
x(t) = e^{A(t - kT_s)} x(kT_s) + \int_{kT_s}^{t} e^{A(t - \tau)} B u(\tau) d\tau
$

Da $u(\tau) = u_k$ während der gesamten Abtastperiode konstant ist, ergibt sich die diskretisierte Zustandsgleichung:

$
x_{k+1} = e^{A T_s} x_k + \left( \int_0^{T_s} e^{A \tau} B d\tau \right) u_k
$

Daher:

$
A_d = e^{A T_s}, \quad B_d = \int_0^{T_s} e^{A \tau} B d\tau
$

Da die Ausgangsgleichung zum Abtastzeitpunkt $k$ direkt abgetastet wird, gilt:

$
C_d = C, \quad D_d = D
$

In MATLAB können wir die Zero-Order-Hold-Diskretisierung mit c2d durchführen.
sysd = c2d(sys, Ts, 'zoh')

## 3.2 MPC-Prinzip und Parameterauswahl

### 3.2.1 **Aktuellen Zustand erfassen**
Zu Beginn jedes Regelungszyklus erfasst MPC den aktuellen Zustand $x(k)$ oder die Ausgabe $y(k)$ des Systems (über Sensoren oder Zustandsschätzer). Dies ist der Ausgangspunkt für die Prädiktion.


### 3.2.2  **Prädiktion initialisieren**
Basierend auf dem aktuellen Zustand $x(k)$ verwendet MPC das dynamische Modell des Systems, um die zukünftigen Zustände und Ausgaben vorherzusagen. Der Prädiktionshorizont umfasst $N$ Schritte, d. h., es werden die Zustände und Ausgaben von $k+1$ bis $k+N$ vorhergesagt.

  Zustandsraummodell (für lineare Systeme):
  $x(k+1) = A x(k) + B u(k)$,
  $y(k) = C x(k) + D u(k)$
  Hierbei sind $A, B, C, D$ die Systemmatrizen und $u(k)$ der Steuereingriff.

### 3.2.3 **Zukünftige Zustände und Ausgaben vorhersagen**
Ausgehend vom aktuellen Zustand $x(k)$ werden die zukünftigen Zustände und Ausgaben schrittweise berechnet:

Der Prädiktionsprozess sieht wie folgt aus:

$
x(k+1) = A x(k) + B u(k)
$

$
x(k+2) = A^2 x(k) + A B u(k) + B u(k+1)
$

$
\vdots
$

$
x(k+N_p) = A^{N_p} x(k) + \sum_{i=0}^{N_p-1} A^i B u(k+N_p-1-i)
$

Ausgangsprädiktion:

$
y(k) = C x(k) + D u(k)
$

$
y(k+1) = C x(k+1) + D u(k+1)
$

$
= C A x(k) + C B u(k) + D u(k+1)
$

$
y(k+2) = C x(k+2) + D u(k+2)
$

$
= C (A^2 x(k) + A B u(k) + B u(k+1)) + D u(k+2)
$

$
\vdots
$

$
y(k+i) = C A^i x(k) + \sum_{j=0}^{i-1} C A^{i-1-j} B u(k+j) + D u(k+i)
$


### 3.2.4 **Optimierungsproblem formulieren**
Basierend auf den Prädiktionsergebnissen wird ein Optimierungsproblem formuliert. Das Ziel ist die Minimierung einer Kostenfunktion, die typischerweise folgende Komponenten enthält:
Folgefehler: Die Ausgabe $y(k+i)$ soll möglichst nahe am Sollwert $y_{\text{ref}}(k+i)$ liegen.
Kosten für Steuereingriffe: Die Änderungen oder Amplituden der Steuereingriffe $u(k+i)$ sollen minimiert werden.

Kostenfunktion:
$
J = \sum_{i=1}^{N} \left( \| y(k+i) - y_{\text{ref}}(k+i) \|^2_{Q} + \| u(k+i) \|^2_{R} \right)
$
Hierbei sind $Q$ und $R$ Gewichtungsmatrizen, die die Bedeutung von Folgefehlern und Steuereingriffen widerspiegeln.


### 3.2.5 **Optimierungsproblem lösen**
Im Prädiktionshorizont wird das Optimierungsproblem gelöst, um die optimale Folge von Steuereingriffen $u(k), u(k+1), \dots, u(k+N-1)$ zu erhalten. Das Optimierungsproblem kann Nebenbedingungen enthalten, wie z. B.:
Beschränkungen der Steuereingriffe: $u_{\text{min}} \leq u(k+i) \leq u_{\text{max}}$

Ausgangsbeschränkungen: $y_{\text{min}} \leq y(k+i) \leq y_{\text{max}}$


### 3.2.6 **Steuereingriff anwenden**
Nach der Optimierung wendet MPC nur den ersten Steuereingriff $u(k)$ auf das System an. Die restlichen Steuereingriffe $u(k+1), \dots, u(k+N-1)$ werden verworfen.


### 3.2.7 **Rollierender Horizont**
Im nächsten Regelungszyklus wird der Zustand des Systems erneut erfasst, der Prädiktionsstartpunkt aktualisiert und die Schritte wiederholt. Diese rollierende Strategie ermöglicht es MPC, sich an Änderungen des Systems und externe Störungen anzupassen.

### 3.2.8 Parameterauswahl
Zuerst wird der Abtastzeitraum ausgewählt, wobei der Abtastzeitraum auf 
$T_s=0,1s$ festgelegt wird.

Anschließend werden der Vorhersagehorizont und der Implementierungshorizont für die Steuerung festgelegt. Der Vorhersagehorizont umfasst 5 Schritte, während der Implementierungshorizont auf 1 Schritt festgelegt ist. Das bedeutet, dass nach jeder Vorhersage der ersten 5 Schritte nur die erste Steuerungseinheit umgesetzt wird, und dieser Prozess wird zyklisch wiederholt.

Dann werden die Gewichtungsmatrizen $Q$ und $R$ ausgewählt, um die Nähe zwischen den Ausgaben und dem Referenzziel zu maximieren und gleichzeitig die Stabilität der Steuerungseinheiten zu gewährleisten. Es wird $Q = \begin{bmatrix}
20 & 10 \\
10 & 5
\end{bmatrix}$ und $R = 3$ gewählt.

Um eine glatte Änderung der Steuerungseinheit zu gewährleisten, wird das Gewicht für die Änderungsrate des Steuerungseingangs $\dot{u}$ auf $R_{\dot{u}} = 30$ festgelegt.

Um sicherzustellen, dass der Laufkatze nicht mit den Grenzen kollidiert und dass die Steuerungseinheit 
$u$ die Begrenzung nicht überschreitet, setzen wir zwei Einschränkungsbedingungen:

$-1 \leq u(k+i) \leq 1$

$0 \leq y(k+i) \leq 1$

## 3.3 Simulationsergebnisse
Die Positionsänderung ist wie im folgenden Bild dargestellt, ohne Überschwingen, und es wird nicht mit den Grenzen kollidieren.

![](Pic/012.PNG)

Die Änderung des Seilwinkels ist wie im folgenden Bild dargestellt, stabil und schnell, ohne anhaltende Schwingungen.

![](Pic/013.PNG)

Die Änderung der Steuerungseinheit ist wie im folgenden Bild dargestellt, und die Veränderung der Steuerungseinheit erfolgt relativ glatt.

![](Pic/014.PNG)


