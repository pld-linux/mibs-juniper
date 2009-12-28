Summary:	MIBs for Juniper Networking Hardware
Summary(pl.UTF-8):	MIB-y dla sprzętu sieciowego Juniper
Name:		mibs-juniper
Version:	7.3
Release:	0.R1.6.1
License:	Unknown
Group:		Applications/System
Requires:	mibs-dirs
Source0:	http://juniper.net/techpubs/software/junos/junos73/juniper-mibs-%{version}R1.6.tgz
# Source0-md5:	380f8475a7f71e093b1dc98e4976c106
Obsoletes:	net-snmp-mibs-juniper
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mibdir	%{_datadir}/mibs

%description
MIBs for Juniper Networking Hardware.

%description -l pl.UTF-8
MIB-y dla sprzętu sieciowego Juniper.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{mibdir}
cp -a JuniperMibs/*.txt $RPM_BUILD_ROOT%{mibdir}
cp -a StandardMibs/*.txt $RPM_BUILD_ROOT%{mibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{mibdir}/*
