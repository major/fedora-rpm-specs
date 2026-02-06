Name:           python-twomemo
Version:        2.1.0
Release:        %{autorelease}
Summary:        Implementation of the namespace `urn:xmpp:omemo:2` for python-omemo

License:        MIT
URL:            https://github.com/Syndace/python-twomemo
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch to allow using protobuf version packaged in Fedora
Patch:          relax-protobuf-version.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  protobuf-compiler
# for docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  texinfo

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Backend implementation for python-omemo, equipping python-omemo with support
for OMEMO under the namespace urn:xmpp:omemo:2 (casually/jokingly referred to
as "twomemo").}

%description %_description

%package -n     python3-twomemo
Summary:        %{summary}

%description -n python3-twomemo %_description

%pyproject_extras_subpkg -n python3-twomemo xml

%package docs
Summary: Documentation for python-twomemo
BuildArch: noarch

%description docs %_description

%prep
%autosetup -p1 -n %{name}-%{version}
# Remove pre-generated files
rm twomemo/twomemo_pb2.py 
rm twomemo/twomemo_pb2.pyi 

%generate_buildrequires
%pyproject_buildrequires -x xml


%build
protoc --python_out=twomemo/  twomemo.proto

%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook twomemo.texi
popd # texinfo
popd # docs

%install
%pyproject_install
%pyproject_save_files -l twomemo
# Install docbook docs
install -pDm0644 docs/texinfo/twomemo.xml \
 %{buildroot}%{_datadir}/help/en/python-twomemo/twomemo.xml

%check
%pyproject_check_import


%files -n python3-twomemo -f %{pyproject_files}
%doc README.md

%files docs
%license LICENSE
%dir  %{_datadir}/help/en/
%lang(en) %{_datadir}/help/en/python-twomemo/

%changelog
%autochangelog
