Name:           plantri
Version:        5.3
Release:        2%{?dist}
Summary:        Generate certain types of planar graphs

%global upstreamver %(sed 's/\\.//g' <<< %{version})

License:        Apache-2.0
URL:            https://users.cecs.anu.edu.au/~bdm/plantri/
Source0:        %{url}plantri%{upstreamver}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
Plantri and fullgen are programs for generating certain types of planar
graphs.  The authors are Gunnar Brinkmann (University of Ghent) and
Brendan McKay (Australian National University).

Graphs are generated in such a way that exactly one member of each
isomorphism class is output without the need for storing them.  The
speed of generation is more than 2,000,000 graphs per second in many
cases, so extremely large classes of graph can be exhaustively listed.

%prep
%autosetup -n %{name}%{upstreamver}

%build
%make_build CFLAGS='%{build_cflags}' LDFLAGS='%{build_ldflags}'

%install
mkdir -p %{buildroot}%{_bindir}
cp -p plantri fullgen %{buildroot}%{_bindir}

%files
%doc fullgen-guide.txt more-counts.txt plantri-guide.txt
%{_bindir}/plantri
%{_bindir}/fullgen

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 28 2023 Jerry James <loganjerry@gmail.com> - 5.3-1
- Initial RPM
