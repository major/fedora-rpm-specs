Name:           python-odfdo
Version:        3.27.3
Release:        %autorelease
Summary:        Python library for OpenDocument Format

License:        Apache-2.0
URL:            https://github.com/jdum/odfdo
Source:         %{url}/archive/v%{version}/odofo-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pillow

%global _description %{expand:
A Python library for programmatically creating, parsing, and editing
OpenDocument Format (ODF) files. It provides an interface for interacting
with .odt, .ods, .odp, and other ODF file types. The library comes with
a set of utilities and recipes for common actions to make it easier to use.}

%description %_description

%package -n     python3-odfdo
Summary:        %{summary}

%description -n python3-odfdo %_description


%prep
%autosetup -p1 -n odfdo-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l odfdo


%check
%pyproject_check_import
%pytest

%files -n python3-odfdo -f %{pyproject_files}
%{_bindir}/odfdo-diff
%{_bindir}/odfdo-flat
%{_bindir}/odfdo-folder
%{_bindir}/odfdo-from-csv
%{_bindir}/odfdo-from-json
%{_bindir}/odfdo-headers
%{_bindir}/odfdo-highlight
%{_bindir}/odfdo-markdown
%{_bindir}/odfdo-meta-print
%{_bindir}/odfdo-meta-update
%{_bindir}/odfdo-replace
%{_bindir}/odfdo-show
%{_bindir}/odfdo-styles
%{_bindir}/odfdo-table-shrink
%{_bindir}/odfdo-to-csv
%{_bindir}/odfdo-to-json
%{_bindir}/odfdo-userfield


%changelog
%autochangelog
