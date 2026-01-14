Name:           R-gtable
Version:        %R_rpm_version 0.3.6
Release:        %autorelease
Summary:        Arrange 'Grobs' in Tables

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Tools to make it easier to work with "tables" of 'grobs'. The 'gtable'
package defines a 'gtable' grob class that specifies a grid along with a
list of grobs and their placement in the grid. Further the package makes
it easy to manipulate and combine 'gtable' objects so that complex
compositions can be build up sequentially.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
