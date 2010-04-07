Summary:	Cisco router emulator controller
Summary(pl.UTF-8):	Kontroler emulatora routera Cisco
Name:		dynagen
Version:	0.11.0
Release:	3
License:	GPL v2+
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/dyna-gen/%{name}-%{version}.tar.gz
# Source0-md5:	3f88b3449b17096dca84d007f0b91b3f
Patch0:		%{name}-debian.patch
URL:		http://dynagen.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-configobj
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dynagen is a text-based front end for Dynamips, that uses the
Hypervisor mode for communication with Dynamips. Dynagen simplifies
building and working with virtual networks:
 - Uses a simple, easy to understand configuration file for specifying
   virtual router hardware configurations
 - Simple syntax for interconnecting routers, bridges, frame-relay and
   ATM switches. No need to deal with NetIOs
 - Can work in a client / server mode, with Dynagen running on your
   workstation communicating to Dynamips running on a back-end server.
   Dynagen can also control multiple Dynamips servers simultaneously
   for distributing large virtual networks across several machines.
 - Provides a management CLI for listing devices, starting, stopping,
   reloading, suspending, and resuming virtual routers.

%description -l pl.UTF-8
Dynagen to tekstowy frontend do Dynamipsa, wykorzystujący tryb
Hypervisor do komunikacji z nim. Upraszcza tworzenie i pracę z
sieciami wirtualnymi:
 - używa prostego, łatwego do zrozumienia pliku konfiguracyjnego do
   określania konfiguracji wirtualnych routerów
 - ma prostą składnię do łączenia routerów, mostów, przełączników
   frame-relay i ATM; nie wymaga znajomości NetIO
 - może działać w trybie klient-serwer, z Dynagenem działającym na
   stacji roboczej komunikującym się z Dynamipsem działającym na
   serwerze
 - udostępnia interfejs linii poleceń do zarządzania, z możliwością
   wypisywania urządzeń i uruchamiania, zatrzymywania,
   przeładowywania, wstrzymywania i wznawiania routerów wirtualnych.

%prep
%setup -q
%patch0 -p1
%{__sed} -i \
	'1s|#!@PYTHON@|#!%{__python}|;
	 s|\(version = "\)@VERSION@",|\1%{version}",|;' \
	setup.py

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root $RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt docs sample_labs
%dir %{_sysconfdir}/dynagen
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dynagen/dynagen.ini
%dir %{_datadir}/dynagen
%{_datadir}/dynagen/configspec
%attr(755,root,root) %{_bindir}/dynagen
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/dynagen-*.egg-info
%{_mandir}/man1/dynagen.1*
