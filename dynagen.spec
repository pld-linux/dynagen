Summary:	Cisco router emulator controller
Summary(pl.UTF-8):	Kontroler emulatora routera Cisco
Name:		dynagen
Version:	0.10.1
Release:	0.1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/dynagen/%{name}-%{version}.tar.gz
# Source0-md5:	4ca26e4b4b8bee61a77f92eace8404d0
Patch0:		%{name}-debian.patch
URL:		http://dynagen.org/
BuildRequires:	python-modules
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cisco 7200 Router Emulator Command Line Interface
Dynagen is a text-based front end for Dynamips, that uses the
Hypervisor mode for communication with Dynamips. Dynagen simplifies
building and working with virtual networks:
  * Uses a simple, easy to understand configuration file for specifying
    virtual router hardware configurations
  * Simple syntax for interconnecting routers, bridges, frame-relay and
    ATM switches. No need to deal with NetIOs
  * Can work in a client / server mode, with Dynagen running on your
    workstation communicating to Dynamips running on a back-end server.
    Dynagen can also control multiple Dynamips servers simultaneously for
    distributing large virtual networks across several machines.
  * Provides a management CLI for listing devices, starting, stopping,
    reloading, suspending, and resuming virtual routers.

#%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1
%{__sed} -i \
	'1s|#!@PYTHON@|#!%{__python}|;
	 s|\(version = "\)@VERSION@",|\1%{version}",|;' \
	$RPM_BUILD_DIR/%{name}-%{version}/setup.py

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT
%{py_ocomp} $RPM_BUILD_ROOT%{py_sitescriptdir}
%{py_postclean}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* COPYING docs sample_labs
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*.py[co]
%{_mandir}/man1/*.1*
