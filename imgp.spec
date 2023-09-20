Name:       imgp
Version:    2.9
Release:    %autorelease
Summary:    Multi-core batch image resizer and rotator

License:    GPL-3.0-only
URL:        https://github.com/jarun/imgp
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make

Requires:   python3-pillow


%description
imgp is a command line image resizer and rotator for JPEG and PNG images. 
It can resize (or thumbnail) and rotate thousands of images in a go,
at lightning speed, while saving significantly on storage.

Powered by multiprocessing, an intelligent adaptive algorithm, 
recursive operations, shell completion scripts, EXIF preservation (and more), 
imgp is a very flexible utility with well-documented easy to use options.

imgp intends to be a stronger replacement of the Nautilus Image Converter 
extension, not tied to any file manager and way faster. On desktop environments 
(like Xfce or LxQt) which do not integrate Nautilus, imgp will save your day.

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '1s/env //' imgp


%build
# Nothing to do


%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/imgp-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  auto-completion/fish/imgp.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_imgp


%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bash-completion/completions/imgp-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/imgp.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_imgp


%changelog
%autochangelog
