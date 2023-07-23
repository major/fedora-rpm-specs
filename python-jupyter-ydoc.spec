Name:           python-jupyter-ydoc
Version:        1.0.2
Release:        3%{?dist}
Summary:        Document structures for collaborative editing using Ypy
License:        BSD-3-Clause
URL:            https://jupyter.org
Source:         %{pypi_source jupyter_ydoc}
# Drop the dependency on nodejs hatch plugin and
# set a version placeholder which we then set by sed
# to the actual version in %%prep.
Patch:          drop-dynamic-version.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
jupyter_ydoc provides Ypy-based data structures for various
documents used in the Jupyter ecosystem.}

%description %_description

%package -n     python3-jupyter-ydoc
Summary:        %{summary}

%description -n python3-jupyter-ydoc %_description


%prep
%autosetup -p1 -n jupyter_ydoc-%{version}
sed -i "s/VERSION_PLACEHOLDER/%{version}/" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyter_ydoc


%check
# There are only two regular tests with these issues:
# - required version of ypy-websocket is too old
#   reported: https://github.com/jupyter-server/jupyter_ydoc/issues/130
# - tests require installation of many JS packages
%pyproject_check_import


%files -n python3-jupyter-ydoc -f %{pyproject_files}


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.12

* Tue May 30 2023 Lumír Balhar <lbalhar@redhat.com> - 1.0.2-1
- Update to 1.0.2 (rhbz#2182754)

* Thu Feb 23 2023 Lumír Balhar <lbalhar@redhat.com> - 0.3.4-1
- Update to 0.3.4 (rhbz#2171414)

* Thu Jan 05 2023 Lumír Balhar <lbalhar@redhat.com> - 0.2.2-1
- Initial package