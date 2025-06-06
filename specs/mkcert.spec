# Generated by go2rpm 1.16.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/FiloSottile/mkcert
%global goipath         github.com/FiloSottile/mkcert
Version:                1.4.4

%gometa -L -f

%global common_description %{expand:
A simple zero-config tool to make locally trusted development certificates with
any names you'd like.}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md

Name:           mkcert
Release:        %autorelease
Summary:        Make and install locally trusted development certificates

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}
Requires:       nss-tools

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
%gobuild -o %{gobuilddir}/bin/mkcert %{goipath}
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/mkcert
%endif

%gopkgfiles

%changelog
%autochangelog
