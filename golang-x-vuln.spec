# https://github.com/golang/vuln
%global goipath		golang.org/x/vuln
%global forgeurl	https://github.com/golang/vuln
Version:		1.0.4

%gometa


%global common_description %{expand:
The database client and tools for the Go vulnerability database.}

%global golicenses      LICENSE PATENTS
%global godocs          doc CONTRIBUTING.md README.md


Name:           %{goname}
Release:        %autorelease
Summary:        Database client and tools for the Go vulnerability database

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck -v -t cmd -t internal

%files
%license LICENSE PATENTS
%doc doc CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
