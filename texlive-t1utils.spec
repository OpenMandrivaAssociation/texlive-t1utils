Name:		texlive-t1utils
Version:	57972
Release:	2
Summary:	Simple Type 1 font manipulation programs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/t1utils
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/t1utils.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/t1utils.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of simple programs for manipulating Adobe Type 1
fonts, comprising: - t1ascii: convert PFB (binary) to PFA
(ascii) fonts; - t1binary: convert PFA to PFB fonts; -
t1disasm: convert PFA or PFB fonts to human-readable and
-editable format; - t1asm: reassemble such editable formats to
a font; - t1unmac: extract font resources from a Macintosh font
file; and - t1mac: generate a Macintosh font from a Type 1
font.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1unmac.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1unmac.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1mac.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1mac.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1disasm.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1disasm.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1binary.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1binary.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1asm.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1asm.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1ascii.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/t1ascii.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
