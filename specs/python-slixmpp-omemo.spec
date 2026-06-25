Name:           python-slixmpp-omemo
Version:        2.2.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OMEMO plugin for Slixmpp

License:        AGPL-3.0-only
URL:            https://github.com/Syndace/slixmpp-omemo
Source:         %{url}/archive/v%{version}/slixmpp-omemo-%{version}.tar.gz
Patch:          no-test-coverage.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
# Additional documentation requirement
BuildRequires:  make
BuildRequires:  python3dist(installer)
BuildRequires:  texinfo

%global _description %{expand:
A plugin for slixmpp offering the OMEMO Multi-End Message and Object Encryption
protocol, based on python-omemo.}

%description %_description

%package -n     python3-slixmpp-omemo
Summary:        %{summary}

%description -n python3-slixmpp-omemo %_description


%prep
%autosetup -p1 -n slixmpp-omemo-%{version}


%generate_buildrequires
%pyproject_buildrequires -x docs


%build
%pyproject_wheel
pushd docs
%python3 -m installer --destdir=tempinstall %{_pyproject_wheeldir}/*.whl
PYTHONPATH="tempinstall/usr/lib/python%{python3_version}/site-packages/:$PYTHONPATH" \
make texinfo
pushd _build
pushd texinfo
makeinfo --docbook slixmpp-omemo.texi
popd
popd
popd

%install
%pyproject_install
%pyproject_save_files -l slixmpp_omemo
mkdir -p %{buildroot}%{_datadir}/help/en/python-slixmpp-omemo
install -m644 docs/_build/texinfo/slixmpp-omemo.xml %{buildroot}%{_datadir}/help/en/python-slixmpp-omemo

%check
%pyproject_check_import
%pytest

%files -n python3-slixmpp-omemo -f %{pyproject_files}
%doc README.md
%dir %{_datadir}/help/en/
%doc %lang(en) %{_datadir}/help/en/python-slixmpp-omemo/

%changelog
%autochangelog
