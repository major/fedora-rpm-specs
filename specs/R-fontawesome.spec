Name:           R-fontawesome
Version:        %R_rpm_version 0.5.3
Release:        %autorelease
Summary:        Easily work with 'Font Awesome' Icons

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Requires:       fontawesome-fonts-web

%description
Easily and flexibly insert 'Font Awesome' icons into 'R Markdown' documents
and 'Shiny' apps. These icons can be inserted into HTML content through inline
'SVG' tags or 'i' tags. There is also a utility function for exporting 'Font
Awesome' icons as 'PNG' images for those situations where raster graphics are
needed.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
rm -fr %{buildroot}%{_R_libdir}/fontawesome/fontawesome
ln -s ../../../fontawesome %{buildroot}%{_R_libdir}/fontawesome
%R_save_files

%check
%R_check \--no-tests

# This and the %%ghost entry in %%files can be removed when F43 reaches EOL
%pretrans -p <lua>
path = "%{_R_libdir}/fontawesome/fontawesome"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%files -f %{R_files}
%ghost %{_R_libdir}/fontawesome/fontawesome.rpmmoved

%changelog
%autochangelog
