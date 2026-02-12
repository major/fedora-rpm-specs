Name:           python-oldmemo
Version:        2.1.0
Release:        %autorelease
Summary:        Backend implementation of the namespace eu.siacs.conversations.axolotl

License:        AGPL-3.0-only
URL:            https://github.com/Syndace/python-oldmemo
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Downstream only patch as Fedora does not yet package newer versions
# of protobuf
Patch:          relax-protobuf.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  protobuf-compiler
# for docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  texinfo

%global _description %{expand:
Backend implementation for python-omemo, equipping python-omemo with support for
OMEMO under the namespace eu.siacs.conversations.axolotl (casually/jokingly
referred to as "oldmemo").

This repository is based on python-twomemo and will be rebased on top of new
commits to that repository regularly, so expect commit hashes to be unstable.
For the same reason, release tags might not be available or point to
non-existing commit hashes.}

%description %_description

%package -n     python3-oldmemo
Summary:        %{summary}

%description -n python3-oldmemo %_description

%pyproject_extras_subpkg -n python3-oldmemo xml


%prep
%autosetup -p1 -n %{name}-%{version}
# Remove pre-generated files
rm oldmemo/oldmemo_pb2.py
rm oldmemo/oldmemo_pb2.pyi

%generate_buildrequires
%pyproject_buildrequires -x xml


%build
protoc --python_out=oldmemo/  oldmemo.proto

%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook oldmemo.texi
popd # texinfo
popd # docs

%install
%pyproject_install
%pyproject_save_files -l oldmemo
# Install docbook docs
install -pDm0644 docs/texinfo/oldmemo.xml \
 %{buildroot}%{_datadir}/help/en/python-oldmemo/oldmemo.xml

%check
%pyproject_check_import


%files -n python3-oldmemo -f %{pyproject_files}
%doc README.md
%dir  %{_datadir}/help/en/
%lang(en) %{_datadir}/help/en/python-oldmemo/

%changelog
%autochangelog
