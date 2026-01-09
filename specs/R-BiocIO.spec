Name:           R-BiocIO
Version:        %R_rpm_version 1.20.0
Release:        %autorelease
Summary:        Standard Input and Output for Bioconductor Packages

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Implements `import()` and `export()` standard generics for importing and
exporting biological data formats. `import()` supports whole-file as well as
chunk-wise iterative import. The `import()` interface optionally provides a
standard mechanism for 'lazy' access via `filter()` (on row or element-like
components of the file resource), `select()` (on column-like components of
the file resource) and `collect()`. The `import()` interface optionally
provides transparent access to remote (e.g. via https) as well as local
access. Developers can register a file extension, e.g., `.loom` for dispatch
from character-based URIs to specific `import()` / `export()` methods based on
classes representing file types, e.g., `LoomFile()`.

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
