Name:           crystal-rpm-macros
Version:        0.2.0
Release:        %autorelease
Summary:        RPM macros and dependency generators for Crystal packaging

License:        GPL-3.0-or-later
URL:            https://codeberg.org/fedora-crystal/crystal-rpm-macros
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pyyaml
BuildRequires:  python3dist(pytest)
Requires:       rpm-build
Requires:       python3-pyyaml

Provides:       crystal-srpm-macros = %{version}-%{release}
Provides:       shards-link = %{version}-%{release}

%description
This package provides RPM macros, file attribute dependency generators,
and the shards-link workspace linker for building and packaging Crystal
applications and shards in Fedora.

%prep
%autosetup -n %{name} -p1

%build
# No compilation needed

%install
install -D -p -m 0644 macros.crystal %{buildroot}%{_rpmmacrodir}/macros.crystal
install -D -p -m 0644 crystalshard.attr %{buildroot}%{_rpmconfigdir}/fileattrs/crystalshard.attr
install -D -p -m 0755 crystalshard.prov %{buildroot}%{_rpmconfigdir}/crystalshard.prov
install -D -p -m 0755 crystalshard.req %{buildroot}%{_rpmconfigdir}/crystalshard.req
install -D -p -m 0755 shards-link %{buildroot}%{_bindir}/shards-link
install -d -m 0755 %{buildroot}%{_datadir}/crystal/shards

%check
PYTHONDONTWRITEBYTECODE=1 %{python3} -B -c "import ast, pathlib; [ast.parse(pathlib.Path(p).read_text()) for p in ('crystalshard.prov', 'crystalshard.req', 'shards-link')]"
PYTHONDONTWRITEBYTECODE=1 %{python3} -B -m pytest -q
PYTHONDONTWRITEBYTECODE=1 %{python3} -B %{buildroot}%{_bindir}/shards-link --version

%files
%license LICENSE
%doc CHANGELOG.rst README.md
%{_bindir}/shards-link
%{_rpmmacrodir}/macros.crystal
%{_rpmconfigdir}/fileattrs/crystalshard.attr
%{_rpmconfigdir}/crystalshard.prov
%{_rpmconfigdir}/crystalshard.req
%dir %{_datadir}/crystal
%dir %{_datadir}/crystal/shards

%changelog
%autochangelog
