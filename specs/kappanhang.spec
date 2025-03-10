# Generated by go2rpm 1.13.1
%bcond_without check

# https://github.com/AD8IM/kappanhang
%global goipath         github.com/AD8IM/kappanhang
%global commit          9751b536b37ab6322e4edee5cbae97f4d1b818f4

%gometa -L -f

%global common_description %{expand:
Remotely open audio channels and a serial port to an Icom RS-BA1 server (for
ex. Icom IC-705 transceiver).}

%global golicenses      LICENSE
%global godocs          README.md

Name:           kappanhang
Version:        0
Release:        %autorelease -p
Summary:        Remotely connect to an Icom RS-BA1 server

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  pulseaudio-libs-devel

%description %{common_description}

%prep
%goprep -A
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/kappanhang %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md demo.gif
%{_bindir}/kappanhang

%changelog
%autochangelog
