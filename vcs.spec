Name:           vcs
Summary:        Tool to create contact sheets (previews) from videos
Version:        1.13.4
Release:        2%{?dist}
License:        LGPLv2+
URL:            https://p.outlyer.net/vcs/
Source0:        https://p.outlyer.net/files/%{name}/%{name}-%{version}.tar.gz
# update syntax for newer ImageMagick
Patch0:         vcs-1.13.4-imagemagick.patch
# egrep warns about its obsolescence in F-38
Patch1:         vcs-1.13.4-grep.patch
BuildArch:      noarch
BuildRequires:  make
# satisfied by ffmpeg-free from Fedora or by ffmpeg from RPMFusion
Requires:       /usr/bin/ffmpeg
Requires:       ImageMagick
Requires:       coreutils
Requires:       gawk


%description
Video Contact Sheet *NIX (vcs for short) is a script that creates a contact
sheet (preview) from videos by taking still captures distributed over the
length of the video. The output image contains useful information on the video
such as codecs, file size, screen size, frame rate, and length.

%prep
%autosetup -p1

# use pcansi terminal instead of pc3, which is not included in ncurses-base
sed -i 's/pc3/pcansi/' vcs


%build
make examples/vcs.conf.example

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} install


%files
%doc CHANGELOG
%doc examples/vcs.conf.example
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/profiles
%{_datadir}/%{name}/profiles/black.conf
%{_datadir}/%{name}/profiles/mosaic.conf
%{_datadir}/%{name}/profiles/white.conf
%{_datadir}/%{name}/profiles/compact.conf
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*


%changelog
* Wed Dec 27 2023 Dan Horák <dan[at]danny.cz> - 1.13.4-2
- updates for F-38+

* Mon Jun 20 2022 Dan Horák <dan[at]danny.cz> - 1.13.4-1
- initial Fedora version
