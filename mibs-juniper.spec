Summary:	MIBs for Juniper Networking Hardware
Summary(pl.UTF-8):   MIB-y dla sprzętu sieciowego Juniper
Name:		net-snmp-mibs-juniper
Version:	7.3
Release:	0.R1.6.1
License:	Unknown
Group:		Applications/System
Source0:	http://juniper.net/techpubs/software/junos/junos73/juniper-mibs-%{version}R1.6.tgz
# Source0-md5:	380f8475a7f71e093b1dc98e4976c106
Requires:	net-snmp-mibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIBs for Juniper Networking Hardware.

%description -l pl.UTF-8
MIB-y dla sprzętu sieciowego Juniper.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/snmp/mibs

install JuniperMibs/*.txt $RPM_BUILD_ROOT%{_datadir}/snmp/mibs
install StandardMibs/*.txt $RPM_BUILD_ROOT%{_datadir}/snmp/mibs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/snmp/mibs/*.*
