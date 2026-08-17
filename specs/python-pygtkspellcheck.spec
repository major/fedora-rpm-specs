%global         srcname         pygtkspellcheck
%global         forgeurl        https://github.com/koehlma/pygtkspellcheck
Version:        5.0.4
Release:        %autorelease
%global         tag             %{version}
%forgemeta

Name:           python-%{srcname}
Summary:        Spellchecking library for GTK

# All code GPL-3.0-or-later
# LGPL-2.1-or-later files below
# pygtkspellcheck-5.0.3/utils/locales/databases/iso3166.xml
# pygtkspellcheck-5.0.3/utils/locales/databases/iso639.xml
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gobject-introspection
BuildRequires:  gtk3-devel
BuildRequires:  python%{python3_pkgversion}-devel
# Documentation dependencies
BuildRequires:  python%{python3_pkgversion}-myst-parser
BuildRequires:  python%{python3_pkgversion}-sphinx
# Check dependency
BuildRequires:  python%{python3_pkgversion}-gobject-devel

BuildArch: noarch

%global _description %{expand:
Python GTK Spellcheck is a simple but quite powerful spellchecking
library for GTK written in pure Python. It's spellchecking component
is based on Enchant and it supports both GTK 3 and 4 via PyGObject.

Features

- spellchecking based on Enchant for GtkTextView
- support for word, line, and multiline ignore regular expressions
- support for both GTK 3 and 4 via PyGObject for Python 3
- configurable extra word characters such as '
- localized names of the available languages based on ISO-Codes
- support for custom ignore tags and hot swap of GtkTextBuffer
- support for Hunspell (LibreOffice) and Aspell (GNU) dictionaries
}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
# TODO: build documentation


%install
%pyproject_install
%pyproject_save_files gtkspellcheck -L


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md
%doc CHANGELOG
%license LICENSE
%doc examples


%changelog
%autochangelog
