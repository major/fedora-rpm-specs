# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/facebookincubator/dhcplb
%global goipath         github.com/facebookincubator/dhcplb
%global commit          c9f4bc7902fc2c2604433b87c0e8ace8255c601b

%gometa -f


%global common_description %{expand:
Dhcplb is Facebook's implementation of a load balancer for DHCP.}

%global golicenses      LICENSE
%global godocs          docs AUTHORS CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Facebook's implementation of a load balancer for DHCP

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%package -n     dhcplb
Summary:        %{summary}

%description -n dhcplb %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/dhcplb %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files -n dhcplb
%license LICENSE
%doc docs AUTHORS CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
