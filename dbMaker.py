from app import db, Food, app

data = [
    Food(id=1, name='Bánh bèo', guide=r"""Nguyên liệu:

200g bột gạo
10g bột năng
200ml nước lạnh
300ml nước nóng
400g tôm đất
30g tôm khô
1 muỗng canh đường
1 muỗng canh nước mắm
1 củ hành tím
2 tép tỏi
50ml dầu ăn
4 nhánh hành lá
3 lát bánh mì gối
400ml nước cốt dừa
70ml nước mắm
50g đường
Cách làm:

Thêm một chút muối vào bột, hòa tan kỹ với nước lạnh. Sau đó, tiếp tục cho nước nóng vào khuấy đều và ủ bột trong 30 phút.
Tôm rửa sạch, lột vỏ, bỏ chỉ đen, thêm đường, mắm, ướp trong vòng 20 phút.
Bánh mì cắt hạt lựu, phơi/sấy khô. Hành lá rửa sạch, xắt nhỏ.
Bánh mì sẽ được chiên với dầu nóng già cho đến khi vàng đều. Đun dầu ăn nóng già, đổ vào tô hành lá đã xắt nhỏ.
Thoa dầu vào lòng chén, làm nóng chén và đổ bột vào hấp từ 6-8 phút.
Nấu cho 400 ml nước dừa khô kẹo lại, bạn cho thêm nước mắm, đường và giấm sao cho vị nước mắm chua ngọt mặn vừa ăn, và tiếp tục nấu sôi. Bạn đợi nước chấm thật nguội mới cho thêm ớt xắt lát vào để ớt nổi lên trên nhìn bắt mắt hơn.
Bày bánh bèo ra dĩa, thêm mỡ hành, nhân tôm và bánh mì chiên giòn lên trên, chan nước mắm vừa đủ vào và thưởng thức.
Chúc bạn thành công và ngon miệng"""),
Food(id=2, name='Bánh bột lọc', guide=r"""Nguyên liệu:
     
Nguyên liệu làm bánh bột lọc:
Vỏ bánh:

400gr bột năng
375gr nước
20gr đường phèn
20gr dầu ăn
2 lít nước luộc bánh
Nhân bánh:

300gr tép
200gr thịt
1/3 muỗng cà phê đường
1/3 muỗng cà phê muối
1/3 muỗng cà phê hạt nêm
1/3 muỗng cà phê bột ngọt
1/3 muỗng cà phê bột điều
Một ít tiêu
Nước mắm:

125gr nước
60gr đường
40gr nước mắm
7gr giấm
5gr muối
Ớt
Lá chuối để gói bánh:

10 lá chuối
Cách làm bánh bột lọc:
Làm vỏ bánh:

Cho bột năng, đường phèn và muối vào tô lớn, trộn đều.
Đun sôi 375gr nước, sau đó cho từ từ vào hỗn hợp bột, khuấy đều cho đến khi bột hòa tan hoàn toàn.
Thêm dầu ăn vào bột, nhồi bằng tay cho đến khi bột mịn và dẻo.
Bọc kín bột bằng màng bọc thực phẩm và để nghỉ trong 30 phút.
Làm nhân bánh:

Sơ chế tôm: Bóc vỏ, bỏ đầu và chỉ đen, rửa sạch.
Sơ chế thịt: Rửa sạch, băm nhuyễn.
Ướp tôm và thịt với đường, muối, hạt nêm, bột ngọt, bột điều và tiêu trong 15 phút.
Gói bánh:

Rửa sạch lá chuối và cắt thành từng miếng vuông vừa đủ để gói bánh.
Bẻ một phần nhỏ mép lá chuối, phết một ít dầu ăn lên trên.
Cho một ít nhân vào giữa miếng lá chuối, gấp lại và gói thành hình vuông hoặc hình tam giác.
Dùng dây chuối hoặc lạt để buộc bánh.
Luộc bánh:

Cho nước vào nồi, thêm một ít muối và đun sôi.
Cho bánh vào nồi, luộc trong khoảng 10-15 phút cho đến khi bánh chín trong.
Vớt bánh ra, để ráo nước.
Pha nước mắm:

Cho nước, đường, nước mắm, giấm và muối vào tô, khuấy đều cho đến khi tan hết.
Ớt băm nhuyễn, cho vào tô nước mắm."""
     ),
Food(id=3, name='Bánh căn', guide=r"""Nguyên liệu:
Nguyên liệu làm bánh căn:
Vỏ bánh:

200gr bột gạo
100gr bột năng
1 muỗng cà phê bột nghệ (tùy chọn)
1 muỗng cà phê hạt nêm
1 muỗng cà phê muối
½ muỗng cà phê tiêu
450ml nước
20gr hành lá cắt nhuyễn
Nhân bánh:

300gr thịt heo xay
1 muỗng cà phê hạt nêm
1 muỗng canh tỏi băm
1 muỗng canh hành tím băm
½ muỗng cà phê tiêu
2 muỗng canh nước mắm
200gr tôm sú
Muối tiêu
Nước chấm:

100ml nước mắm
100ml nước lọc
50gr đường
2 muỗng canh nước cốt chanh
1 muỗng canh tỏi băm
1 muỗng canh ớt băm
½ muỗng cà phê tiêu
Rau sống:

Xà lách
Húng lủi
Rau mùi
giá đỗ
Dụng cụ:

Khuôn bánh căn
Chảo
Bếp
Cách làm bánh căn:
Làm vỏ bánh:

Cho bột gạo, bột năng, bột nghệ (nếu dùng), hạt nêm, muối, tiêu và nước vào tô lớn, khuấy đều cho đến khi hỗn hợp hòa quyện.
Thêm hành lá cắt nhuyễn vào hỗn hợp bột, khuấy nhẹ và để bột nghỉ 1 tiếng.
Làm nhân bánh:

Ướp thịt heo xay với hạt nêm, tỏi băm, hành tím băm, tiêu, nước mắm trong 30 phút.
Bóc vỏ tôm sú, bỏ đầu và chỉ đen, rửa sạch.
Làm nước chấm:

Cho nước mắm, nước lọc, đường, nước cốt chanh, tỏi băm, ớt băm và tiêu vào tô, khuấy đều cho đến khi tan hết.
Làm rau sống:

Rửa sạch xà lách, húng lủi, rau mùi và giá đỗ, để ráo nước.
Đổ bánh căn:

Bắc khuôn bánh căn lên bếp, đun nóng.
Cho một ít dầu ăn vào khuôn.
Múc một vá canh bột vào khuôn, tráng đều xung quanh.
Cho một ít nhân thịt và tôm vào giữa bánh.
Đậy nắp khuôn lại và đun trong khoảng 2-3 phút cho đến khi bánh chín.
Gỡ bánh ra khỏi khuôn và bày ra đĩa.
     """
),
Food(id=4, name='Bánh canh', guide=r"""Nguyên liệu:
Nguyên liệu làm bánh canh:
Sợi bánh canh:

250g bột gạo
150g bột năng
Muối, nước lọc, dầu ăn
Nồi, khuôn ép tạo hình bánh canh (hoặc có thể mua sẵn sợi bánh canh)
Nước dùng:

Xương heo (hoặc gà)
Cá lóc (hoặc tôm, mực)
1 củ hành tây
4 củ hành tím
3 tép tỏi
2 củ cà rốt
1 củ gừng
Hành lá, ngò rí
Gia vị: muối, đường, hạt nêm, nước mắm
Rau ăn kèm:

Xà lách
Húng lủi
Rau mùi
Giá đỗ
Ớt
Chanh, ớt băm

Cách làm bánh canh:
Làm sợi bánh canh:

Trộn đều bột gạo, bột năng, muối và nước lọc.
Nhồi bột đến khi mịn và dẻo.
Chia bột thành từng phần nhỏ, cán mỏng rồi cắt thành sợi.
Hoặc có thể mua sẵn sợi bánh canh.
Nấu nước dùng:

Rửa sạch xương heo (hoặc gà) và cho vào nồi.
Thêm nước vào nồi và hầm trong khoảng 1 tiếng.
Nêm nếm gia vị cho vừa ăn.
Phi thơm hành tím, tỏi băm cùng với dầu ăn.
Cho cá lóc (hoặc tôm, mực) vào xào sơ.
Cho cá vào nồi nước dùng, hầm thêm khoảng 30 phút.
Gọt vỏ và cắt khúc cà rốt, hành tây.
Cho cà rốt và hành tây vào nồi nước dùng, hầm thêm 15 phút.
Nêm nếm gia vị cho vừa ăn."""),
Food(id=5, name='Bánh chưng', guide=r"""Nguyên liệu:
     
Nguyên liệu làm bánh chưng:
Vỏ bánh:

2kg gạo nếp cái hoa vàng
30 lá dong
1 bó lạt tre hoặc lạt giang
Nhân bánh:

1kg thịt ba chỉ
600gr đậu xanh đã bóc vỏ
Muối, tiêu, đường, hạt nêm
Gia vị ướp thịt:

Hành tím băm
Tỏi băm
Nước mắm
Tiêu
Đường
Cách làm bánh chưng:
Sơ chế nguyên liệu:

Vo gạo nếp và ngâm qua đêm.
Đậu xanh vo sạch và ngâm 4 tiếng.
Thịt ba chỉ rửa sạch, cắt miếng vừa ăn. Ướp thịt với hành tím băm, tỏi băm, nước mắm, tiêu, đường trong 30 phút.
Gói bánh:

Rửa sạch lá dong và lau khô.
Lót lá dong vào khuôn vuông, gấp mép lá lại.
Cho một lớp gạo nếp vào khuôn, dàn đều.
Cho nhân đậu xanh và thịt ba chỉ vào giữa lớp gạo nếp.
Cho tiếp một lớp gạo nếp lên trên, dàn đều.
Gấp lá dong lại và buộc bằng lạt tre hoặc lạt giang.
Luộc bánh:

Cho bánh chưng vào nồi lớn, đổ nước vào sao cho ngập bánh.
Đun sôi nước và luộc bánh trong khoảng 8-10 tiếng.
Sau khi luộc chín, vớt bánh ra để ráo nước."""),
Food(id=6, name='Bánh cuốn', guide=r"""Nguyên liệu:
     
Nguyên liệu làm bánh cuốn:
Vỏ bánh:

200gr bột gạo
100gr bột năng
600ml nước ấm
1 muỗng canh dầu ăn
1/2 muỗng cà phê muối
Nhân bánh:

300gr thịt nạc xay
200gr nấm hương
100gr mộc nhĩ
2 củ hành tím
1 củ hành tây
Gia vị: muối, tiêu, nước mắm, hạt nêm, đường
Nước mắm chấm:

100ml nước mắm
50ml nước lọc
2 muỗng canh đường
1 muỗng canh nước cốt chanh
1 muỗng cà phê ớt băm
Tỏi băm
Rau sống:

Xà lách
Rau mùi
Húng lủi
Giá đỗ
Cách làm bánh cuốn:
Làm vỏ bánh:

Trộn đều bột gạo, bột năng, muối và nước ấm trong tô lớn.
Khuấy đều cho đến khi bột hòa tan hoàn toàn và không bị vón cục.
Thêm dầu ăn vào bột, khuấy đều.
Đậy kín tô bột bằng màng bọc thực phẩm và để nghỉ trong 30 phút.
Làm nhân bánh:

Ngâm nấm hương và mộc nhĩ trong nước ấm cho nở mềm.
Vớt ra, rửa sạch và cắt nhỏ.
Phi thơm hành tím băm với dầu ăn.
Cho thịt xay vào xào săn.
Thêm nấm hương, mộc nhĩ, hành tây vào xào cùng.
Nêm nếm gia vị cho vừa ăn.
Làm nước mắm chấm:

Cho nước mắm, nước lọc, đường, nước cốt chanh, ớt băm và tỏi băm vào tô.
Khuấy đều cho đến khi tan hết.
Làm rau sống:

Rửa sạch xà lách, rau mùi, húng lủi và giá đỗ.
Để ráo nước.
Tráng bánh:

Bắc chảo chống dính lên bếp, đun nóng.
Múc một vá canh bột vào chảo, tráng đều thành một lớp mỏng.
Đậy nắp chảo lại và đun trong khoảng 30 giây cho đến khi bánh chín.
Dùng phới mỏng gỡ bánh ra khỏi chảo.
Gói bánh:

Cho một ít nhân vào giữa miếng bánh.
Gấp hai mép bánh lại và cuộn tròn."""),
Food(id=7, name='Bánh đúc', guide=r"""Nguyên liệu:
Nguyên liệu làm bánh đúc:
Bánh đúc:

200gr bột gạo tẻ
100gr bột năng
600ml nước
1 muỗng cà phê muối
2 muỗng canh dầu ăn
Nhân bánh (tùy chọn):

Thịt xay
Nấm hương
Mộc nhĩ
Hành tím
Hành tây
Gia vị: muối, tiêu, nước mắm, hạt nêm, đường
Rau sống: xà lách, rau mùi, húng lủi, giá đỗ
Nước mắm chấm:

Nước mắm
Nước lọc
Đường
Nước cốt chanh
Ớt băm
Tỏi băm
Cách làm bánh đúc:
Làm bánh đúc:

Trộn đều bột gạo tẻ, bột năng, muối và nước trong tô lớn.
Khuấy đều cho đến khi bột hòa tan hoàn toàn và không bị vón cục.
Để bột nghỉ trong 30 phút.
Bắc nồi lên bếp, đun sôi nước.
Cho từ từ hỗn hợp bột vào nồi, khuấy đều tay để tránh bột bị vón cục.
Nấu với lửa nhỏ cho đến khi bột sánh mịn và đặc lại.
Thêm dầu ăn vào bột, khuấy đều.
Tắt bếp và đổ bột ra khuôn.
Để bánh nguội và đông lại.
Cắt bánh thành từng miếng vừa ăn.
Làm nhân bánh (tùy chọn):

Ngâm nấm hương và mộc nhĩ trong nước ấm cho nở mềm.
Vớt ra, rửa sạch và cắt nhỏ.
Phi thơm hành tím băm với dầu ăn.
Cho thịt xay vào xào săn.
Thêm nấm hương, mộc nhĩ, hành tây vào xào cùng.
Nêm nếm gia vị cho vừa ăn.
Làm nước mắm chấm:

Cho nước mắm, nước lọc, đường, nước cốt chanh, ớt băm và tỏi băm vào tô.
Khuấy đều cho đến khi tan hết.
Làm rau sống:

Rửa sạch xà lách, rau mùi, húng lủi và giá đỗ.
Để ráo nước."""),
Food(id=8, name='Bánh giò', guide=r"""Nguyên liệu:
Vỏ bánh:

320gr bột gạo tẻ
80gr bột năng
1 muỗng cà phê muối
1.5 lít nước dùng gà
2 muỗng canh dầu ăn
Nhân bánh:

200gr thịt heo xay
100gr nấm hương
50gr mộc nhĩ
2 củ hành tím
1 củ hành tây
Gia vị: muối, tiêu, nước mắm, hạt nêm, đường
10 quả trứng cút (có thể thay thế bằng trứng gà hoặc vịt)
Lá chuối để gói bánh:

10 lá chuối
Cách làm bánh giò:
Làm vỏ bánh:

Hòa tan bột gạo tẻ, bột năng và muối vào nước dùng gà.
Khuấy đều cho đến khi hỗn hợp hòa tan hoàn toàn.
Bắc nồi lên bếp, đun với lửa nhỏ.
Khuấy liên tục cho đến khi bột sánh mịn và đặc lại.
Thêm dầu ăn vào bột, khuấy đều.
Tắt bếp và để bột nguội bớt.
Làm nhân bánh:

Ngâm nấm hương và mộc nhĩ trong nước ấm cho nở mềm.
Vớt ra, rửa sạch và cắt nhỏ.
Phi thơm hành tím băm với dầu ăn.
Cho thịt heo xay vào xào săn.
Thêm nấm hương, mộc nhĩ, hành tây vào xào cùng.
Nêm nếm gia vị cho vừa ăn.
Luộc chín trứng cút.
Gói bánh:

Rửa sạch lá chuối và cắt thành từng miếng vuông vừa đủ để gói bánh.
Cho một ít nhân vào giữa miếng lá chuối.
Thêm 1 quả trứng cút vào giữa nhân.
Gấp lá chuối lại và buộc bằng dây chuối hoặc lạt.
Hấp bánh:

Cho nước vào nồi hấp, đun sôi.
Xếp bánh giò vào nồi hấp, hấp trong khoảng 30-40 phút cho đến khi bánh chín."""),
Food(id=9, name='Bánh khọt', guide=r"""Nguyên liệu:
Vỏ bánh:

250gr bột gạo
200ml nước cốt dừa
50gr bột chiên giòn
15gr bột năng
10gr bột nghệ (tùy chọn)
70gr cơm nguội
200ml nước dừa
300gr tôm
1 muỗng cà phê muối
1 muỗng cà phê đường
½ muỗng cà phê tiêu
Hành lá
Nước mắm chấm:

100ml nước mắm
100ml nước lọc
50gr đường
2 muỗng canh nước cốt chanh
1 muỗng canh tỏi băm
1 muỗng canh ớt băm
½ muỗng cà phê tiêu
Rau sống:

Xà lách
Húng lủi
Rau mùi
Giá đỗ
Dụng cụ:

Khuôn bánh khọt
Chảo
Bếp
Cách làm bánh khọt:
Làm bột bánh:

Cho bột gạo, bột chiên giòn, bột năng, bột nghệ (nếu dùng), muối, đường, tiêu, nước cốt dừa và nước dừa vào tô lớn, khuấy đều cho đến khi hỗn hợp hòa quyện.
Thêm cơm nguội vào hỗn hợp bột, khuấy đều và để bột nghỉ trong 30 phút.
Nêm nếm lại gia vị cho vừa ăn.
Làm nhân bánh:

Bóc vỏ tôm, bỏ đầu và chỉ đen, rửa sạch.
Ướp tôm với một ít muối và tiêu trong 15 phút.
Làm nước mắm chấm:

Cho nước mắm, nước lọc, đường, nước cốt chanh, tỏi băm, ớt băm và tiêu vào tô, khuấy đều cho đến khi tan hết.
Làm rau sống:

Rửa sạch xà lách, húng lủi, rau mùi và giá đỗ, để ráo nước.
Đổ bánh khọt:

Bắc khuôn bánh khọt lên bếp, đun nóng.
Cho một ít dầu ăn vào khuôn.
Múc một vá canh bột vào khuôn, tráng đều xung quanh.
Cho một ít nhân tôm vào giữa bánh.
Đậy nắp khuôn lại và đun trong khoảng 2-3 phút cho đến khi bánh chín.
Gỡ bánh ra khỏi khuôn và bày ra đĩa."""),
Food(id=10, name='Bánh mì', guide=r"""Nguyên liệu:
Nguyên liệu chính:

500g bột mì số 11
350ml nước ấm (30-35°C)
7g men nở instant
10g muối
20g đường
20g dầu ăn
Nguyên liệu phụ (tùy chọn):

1 quả trứng gà (để phết mặt bánh)
Sữa tươi không đường (để phết mặt bánh)
Mè trắng (để rắc lên mặt bánh)
Hạt chia (để rắc lên mặt bánh)
Dụng cụ:

Bát tô lớn
Cân
Thìa/muỗng
Máy nhồi bột (hoặc có thể nhồi bằng tay)
Khuôn nướng bánh mì
Dao
Giấy nến (baking paper)
Cách làm bánh mì:
Bước 1: Trộn bột

Cho bột mì, men nở, muối, đường và dầu ăn vào tô lớn.
Trộn đều nguyên liệu bằng tay hoặc máy nhồi bột cho đến khi hỗn hợp hòa quyện.
Thêm nước ấm vào từ từ và tiếp tục nhồi bột cho đến khi mịn và dẻo.
Nhồi bột trong khoảng 10-15 phút bằng tay hoặc 5-7 phút bằng máy nhồi bột.
Bọc kín tô bột bằng màng bọc thực phẩm và ủ bột ở nơi ấm áp trong khoảng 1-2 tiếng cho đến khi bột nở gấp đôi.
Bước 2: Tạo hình bánh mì

Lấy bột ra khỏi tô và chia thành từng phần bằng nhau (khoảng 250g/phần).
Vo tròn từng phần bột và để nghỉ trong 10 phút.
Tạo hình bánh mì theo ý thích (hình ổ, hình baguette,...)
Đặt bánh mì vào khuôn nướng có lót sẵn giấy nến.
Phủ khăn ẩm lên mặt bánh và ủ thêm 30 phút cho đến khi bánh nở gấp đôi.
Bước 3: Nướng bánh mì

Làm nóng lò nướng ở 180°C trước 10 phút.
Phết mặt bánh mì với trứng gà hoặc sữa tươi không đường.
Rắc mè trắng hoặc hạt chia lên mặt bánh (tùy chọn).
Nướng bánh mì trong khoảng 30-35 phút cho đến khi vàng đều.
"""),
Food(id=11, name='Bánh pía', guide=r"""Nguyên liệu:
Phần vỏ bánh:

400g bột mì đa dụng
250gr đậu xanh đã cà vỏ
200gr sầu riêng (đã tách hạt)
100gr mỡ nước
100gr đường
80gr bột năng
50gr trứng muối
40gr nước cốt dừa
20gr muối
1 muỗng cà phê bột nở
1 muỗng cà phê vani
1 muỗng cà phê rượu mai quế
1/2 muỗng cà phê baking soda
Phần nhân bánh:

300gr đậu xanh đã cà vỏ
150gr đường
100gr mỡ phần
12 lòng đỏ trứng muối
200ml rượu trắng
4 muỗng canh dầu ăn
1 quả trứng gà
1 muỗng canh bột nếp rang (bột bánh dẻo)
Dụng cụ:

Khuôn bánh pía
Chảo chống dính
Máy xay sinh tố
Cọ quét bánh
Dao
Giấy nến
Cách làm bánh pía:
Bước 1: Sơ chế nguyên liệu

Rửa sạch đậu xanh, ngâm nước trong 4-6 tiếng cho nở mềm.
Vớt đậu xanh ra, vớt ráo nước và hấp chín.
Cho đậu xanh vào máy xay sinh tố, xay nhuyễn cùng với đường, mỡ phần, lòng đỏ trứng muối, rượu trắng, dầu ăn, trứng gà và bột nếp rang.
Trộn đều hỗn hợp nhân cho đến khi mịn và dẻo.
Chia nhân bánh thành từng viên nhỏ, vo tròn và để riêng.
Sầu riêng tách hạt, bỏ xơ, xay nhuyễn cùng với đường, nước cốt dừa, vani, rượu mai quế và baking soda.
Trộn đều hỗn hợp sầu riêng cho đến khi mịn và dẻo.
Chia hỗn hợp sầu riêng thành từng viên nhỏ, vo tròn và để riêng.
Bước 2: Làm vỏ bánh

Cho bột mì, bột năng, muối và bột nở vào tô lớn, trộn đều.
Thêm nước vào từ từ và nhào bột cho đến khi mịn và dẻo.
Bọc kín tô bột bằng màng bọc thực phẩm và ủ bột ở nơi ấm áp trong khoảng 30 phút.
Chia bột thành từng phần nhỏ, vo tròn và cán mỏng thành từng miếng.
Bước 3: Gói bánh

Cho một viên nhân đậu xanh vào giữa miếng vỏ bánh.
Gấp mép bánh lại và ấn chặt để tạo thành hình bánh pía.
Dùng cọ quét bánh lên mặt bánh.
Bước 4: Nướng bánh

Làm nóng lò nướng ở 180°C trước 10 phút.
Xếp bánh pía lên khay nướng có lót sẵn giấy nến.
Nướng bánh trong khoảng 20-25 phút cho đến khi bánh chín vàng đều."""),
Food(id=12, name='Bánh tét', guide=r"""Nguyên liệu:
Nguyên liệu:

Vỏ bánh:
2kg nếp cái hoa vàng
Muối
Lá chuối tươi
Dây lạt
Nhân bánh:
1kg thịt ba chỉ
500g đậu xanh
Muối, tiêu, đường, hạt nêm
Hành tím
Hành lá
Gia vị chấm:
Nước mắm
Tỏi
Ớt
Chanh
Đường
Cách làm:

Bước 1: Sơ chế nguyên liệu:

Nếp vo sạch, ngâm nước trong 8 tiếng cho nở mềm. Vớt ra, vớt ráo nước và trộn đều với 1 muỗng cà phê muối.
Đậu xanh đãi vỏ, ngâm nước trong 4 tiếng cho nở mềm. Vớt ra, vớt ráo nước và hấp chín.
Thịt ba chỉ rửa sạch, cắt khúc vừa ăn. Ướp thịt với 1 muỗng cà phê muối, 1 muỗng cà phê tiêu, 1 muỗng cà phê đường, 1 muỗng cà phê hạt nêm, hành tím băm và hành lá cắt nhỏ trong 30 phút.
Lá chuối rửa sạch, phơi ráo. Dây lạt ngâm nước cho mềm.
Bước 2: Gói bánh:

Trải 2 lá chuối lên mặt phẳng, xếp chéo nhau. Cho 1 lớp nếp vào giữa lá chuối, dàn đều.
Cho 1 lớp nhân đậu xanh lên trên nếp.
Cho 1 lớp thịt ba chỉ lên trên đậu xanh.
Cuộn lá chuối lại và buộc chặt bằng dây lạt.
Bước 3: Nấu bánh:

Xếp bánh tét vào nồi lớn, đổ nước vào nồi sao cho nước ngập bánh.
Nấu bánh với lửa lớn trong khoảng 4-5 tiếng cho đến khi bánh chín mềm.
Vớt bánh ra, để ráo nước và treo lên cao cho bánh ráo hẳn."""),
Food(id=13, name='Bánh tráng nướng', guide=r"""Nguyên liệu:
Nguyên liệu chính:

Bánh tráng: 5-6 cái (tùy theo sở thích)
Thịt heo xay: 100gr
Xúc xích: 2 cây
Trứng gà: 2 quả
Tép khô: 50gr
Hành lá: 5 nhánh
Hành phi: 1 muỗng canh
Bơ lạt: 1 muỗng canh
Sa tế: 1 muỗng canh
Mayonnaise: 1 muỗng canh
Muối, tiêu, dầu ăn
Nguyên liệu phụ (tùy chọn):

Phô mai mozzarella: 50gr
Bò khô: 50gr
Khô mực: 50gr
Ớt tươi: 1 quả
Dụng cụ:

Chảo chống dính hoặc lò nướng
Cọ quét
Dao, thớt
Dĩa
Cách làm bánh tráng nướng:
Bước 1: Sơ chế nguyên liệu:

Bánh tráng nướng qua lửa cho mềm dẻo.
Thịt heo xay ướp với 1 muỗng cà phê muối, 1/2 muỗng cà phê tiêu trong 10 phút.
Xúc xích cắt thành từng khoanh mỏng.
Trứng gà đánh tan.
Tép khô ngâm nước cho mềm, vớt ra để ráo.
Hành lá cắt nhỏ.
Phô mai mozzarella cắt thành từng miếng nhỏ (tùy chọn).
Bò khô, khô mực xé nhỏ (tùy chọn).
Ớt tươi cắt lát (tùy chọn).
Bước 2: Nướng bánh tráng:

Cách 1: Nướng bằng chảo chống dính:

Bắc chảo chống dính lên bếp, cho 1 muỗng canh dầu ăn vào chảo, đun nóng.
Quét 1 lớp bơ lạt lên mặt bánh tráng.
Cho thịt heo xay vào giữa bánh tráng, dàn đều.
Cho tiếp xúc xích, trứng gà, tép khô, hành lá, hành phi, sa tế, mayonnaise lên trên.
Nướng bánh tráng với lửa vừa cho đến khi thịt heo xay chín, trứng gà và phô mai (nếu có) tan chảy.
Gấp bánh tráng lại và cắt thành từng miếng vừa ăn.
Cách 2: Nướng bằng lò nướng:

Làm nóng lò nướng ở 180°C trước 10 phút.
Xếp bánh tráng lên khay nướng có lót sẵn giấy nến.
Cho nguyên liệu lên trên bánh tráng tương tự như cách nướng bằng chảo chống dính.
Nướng bánh tráng trong khoảng 10-15 phút cho đến khi thịt heo xay chín, trứng gà và phô mai (nếu có) tan chảy.
Gấp bánh tráng lại và cắt thành từng miếng vừa ăn."""),
Food(id=14, name='Bánh xèo', guide=r"""Nguyên liệu:
Phần vỏ bánh:

500gr bột bánh xèo
250ml nước lọc
250ml nước cốt dừa
1 muỗng cà phê muối
1/2 muỗng cà phê bột nghệ (tùy chọn)
Hành lá cắt nhỏ
1 muỗng canh dầu ăn
Phần nhân bánh:

200gr thịt heo ba chỉ
200gr tôm sú
100gr giá đỗ
100gr nấm
1 củ hành tây
1 củ cà rốt
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
1 muỗng cà phê hạt nêm
1 muỗng canh dầu ăn
Nước mắm chấm:

200ml nước mắm
200ml nước lọc
100gr đường
2 muỗng canh nước cốt chanh
1 muỗng canh tỏi băm
1 muỗng canh ớt băm
Cà rốt bào sợi
Rau sống (xà lách, húng lủi, rau thơm,...)
Dụng cụ:

Chảo chống dính
Khò gas hoặc bếp than
Tô, chén
Muỗng, dao
Giấy nến
Cách làm bánh xèo:
Bước 1: Sơ chế nguyên liệu:

Phần vỏ bánh:
Bột bánh xèo pha với nước lọc, nước cốt dừa, muối, bột nghệ (nếu dùng), hành lá cắt nhỏ và dầu ăn, khuấy đều cho đến khi bột tan mịn và không bị vón cục. Để bột nghỉ trong 30 phút.
Phần nhân bánh:
Thịt heo ba chỉ rửa sạch, cắt mỏng. Ướp thịt với 1/2 muỗng cà phê muối, 1/4 muỗng cà phê tiêu và 1/2 muỗng cà phê hạt nêm trong 15 phút.
Tôm sú rửa sạch, bóc vỏ, bỏ đầu và chỉ đen. Ướp tôm với 1/2 muỗng cà phê muối, 1/4 muỗng cà phê tiêu và 1/2 muỗng cà phê hạt nêm trong 15 phút.
Giá đỗ rửa sạch, để ráo nước.
Nấm rửa sạch, cắt lát.
Hành tây và cà rốt gọt vỏ, rửa sạch, bào sợi.
Nước mắm chấm:
Pha nước mắm với nước lọc, đường, nước cốt chanh, tỏi băm và ớt băm, khuấy đều cho đến khi tan hết.
Bào cà rốt thành sợi.
Rửa sạch rau sống, để ráo nước.
Bước 2: Làm bánh xèo:

Bắc chảo chống dính lên bếp, cho 1 muỗng canh dầu ăn vào chảo, đun nóng.
Múc một vá canh bột bánh xèo vào chảo, tráng đều xung quanh.
Cho một ít nhân thịt heo ba chỉ, tôm sú, giá đỗ, nấm, hành tây và cà rốt vào giữa bánh.
Gập bánh lại và chiên cho đến khi bánh chín vàng đều hai mặt.
Dùng khò gas hoặc bếp than để nướng bánh xèo (tùy chọn)."""),
Food(id=15, name='Bún bò huế', guide=r"""Nguyên liệu:
Nguyên liệu:

Xương:

1 kg xương ống heo
500 gr xương bò
1 củ gừng
2 cây sả
1 muỗng cà phê muối
Nước dùng:

2 muỗng canh mắm ruốc Huế
2 lít nước
1 muỗng cà phê muối
1 muỗng cà phê đường
1 muỗng canh dầu ăn
1 củ hành tây
1 củ cà rốt
2 cây sả
1 muỗng canh bột bắp (hoặc bột năng)
Thịt:

500 gr bắp bò
500 gr giò heo
500 gr thịt nạc vai
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
1 muỗng cà phê hạt nêm
1 muỗng canh dầu ăn
Chả Huế:

300 gr thịt nạc vai
100 gr mỡ heo
100 gr tôm sú
1 muỗng canh bột năng
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
1 muỗng cà phê hạt nêm
1 muỗng canh dầu ăn
1 muỗng canh hành tím băm
1 muỗng cà phê tiêu hột
Rau sống:

Rau sống ăn kèm bún bò Huế (xà lách, hoa chuối, húng lủi, rau mùi, giá đỗ,...)
Ớt tươi
Chanh
Gia vị:

Muối tiêu chanh
Tương ớt
Sa tế
Dụng cụ:

Nồi lớn
Dao thớt
Tô chén
Muỗng, vá
Khuôn chả Huế (hoặc khuôn hấp)
Giấy nến
Cách nấu bún bò Huế:
Bước 1: Sơ chế nguyên liệu:

Xương: Rửa sạch xương ống heo và xương bò, cho vào nồi cùng với 1 củ gừng đập dập và 2 cây sả đập dập. Nấu nước sôi, hớt bọt, sau đó vớt xương ra, rửa sạch và cho lại vào nồi. Thêm 1 muỗng cà phê muối vào nồi nước dùng.
Nước dùng: Pha 2 muỗng canh mắm ruốc Huế với 100ml nước, khuấy đều cho tan. Phi thơm 1 muỗng canh dầu ăn với 1 củ hành tây thái múi cau và 1 củ cà rốt thái khúc. Cho hành tây, cà rốt và mắm ruốc đã pha vào nồi nước dùng. Nấu sôi nước dùng, sau đó hạ nhỏ lửa và hầm trong khoảng 2 tiếng cho đến khi nước dùng ngọt thanh.
Thịt:
Bắp bò rửa sạch, trụng qua nước sôi để khử mùi hôi. Ướp bắp bò với 1 muỗng cà phê muối, 1/2 muỗng cà phê tiêu và 1 muỗng cà phê hạt nêm trong 15 phút.
Giò heo rửa sạch, chặt khúc vừa ăn. Ướp giò heo với 1 muỗng cà phê muối, 1/2 muỗng cà phê tiêu và 1 muỗng cà phê hạt nêm trong 15 phút.
Thịt nạc vai rửa sạch, cắt mỏng. Ướp thịt nạc vai với 1 muỗng cà phê muối, 1/2 muỗng cà phê tiêu và 1 muỗng cà phê hạt nêm trong 15 phút.
Chả Huế:
Thịt nạc vai, mỡ heo và tôm sú xay nhuyễn. Ướp hỗn hợp với 1 muỗng cà phê muối, 1/2 muỗng cà phê tiêu, 1 muỗng cà phê hạt nêm, 1 muỗng canh hành tím băm và 1 muỗng cà phê tiêu hột trong 15 phút.
Cho hỗn hợp chả Huế vào khuôn chả Huế hoặc khuôn hấp, hấp chín trong khoảng 20 phút.
Rau sống: Rửa sạch rau sống, để ráo nước. Ớt tươi cắt lát. Chanh cắt múi cau.
Bước 2: Nấu bún bò Huế:

Cho bắp bò, giò heo và thịt nạc vai vào nồi nước dùng, nấu sôi. Hớt bọt và hạ nhỏ lửa, hầm trong khoảng 1 tiếng cho đến khi thịt chín mềm.
Vớt bắp bò, giò heo và thịt nạc vai ra, cắt thành từng miếng vừa ăn.
Hòa tan 1 muỗng canh bột bắp (hoặc bột năng) với 100ml nước, khuấy đều. Cho từ từ hỗn hợp bột bắp vào nồi nước dùng, khuấy đều cho đến khi nước dùng sệt lại.
Nêm nếm gia vị cho vừa ăn, bao gồm muối, đường và hạt nêm."""),
Food(id=16, name='Bún đậu mắm tôm', guide=r"""Nguyên liệu:
Nguyên liệu:

Bún:

500gr bún lá
2 lít nước
1 muỗng cà phê muối
Đậu hũ:

500gr đậu hũ
500ml dầu ăn
1 muỗng cà phê muối
Thịt:

500gr thịt ba chỉ
500gr thịt chân giò
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
1 muỗng cà phê hạt nêm
1 muỗng canh dầu ăn
Mắm tôm:

3 muỗng canh mắm tôm ngon
1 muỗng canh đường
1 quả quất
1 quả ớt tươi
1 muỗng canh dầu ăn
1 củ hành tím
Nước cốt chanh
Tỏi băm
Rau sống:

Rau sống ăn kèm bún đậu mắm tôm (xà lách, hoa chuối, húng lủi, rau mùi, giá đỗ,...)
Ớt tươi
Chanh
Gia vị:

Muối tiêu chanh
Tương ớt
Sa tế
Dụng cụ:

Nồi lớn
Chảo rán
Dao thớt
Tô chén
Muỗng, vá
Khuôn rán đậu hũ (hoặc chảo chống dính)
Giấy nến
Cách nấu bún đậu mắm tôm:
Bước 1: Sơ chế nguyên liệu:

Bún: Nấu sôi 2 lít nước với 1 muỗng cà phê muối. Cho bún lá vào chần sơ qua, vớt ra để ráo nước.
Đậu hũ: Cắt đậu hũ thành từng miếng vừa ăn. Cho đậu hũ vào tô, ướp với 1 muỗng cà phê muối trong 15 phút. Rán đậu hũ vàng giòn với dầu ăn.
Thịt:
Thịt ba chỉ rửa sạch, cắt miếng vừa ăn. Ướp thịt ba chỉ với 1 muỗng cà phê muối, 1/2 muỗng cà phê tiêu và 1 muỗng cà phê hạt nêm trong 15 phút.
Thịt chân giò rửa sạch, trụng qua nước sôi để khử mùi hôi. Ướp thịt chân giò với 1 muỗng cà phê muối, 1/2 muỗng cà phê tiêu và 1 muỗng cà phê hạt nêm trong 15 phút.
Rán thịt ba chỉ và thịt chân giò vàng giòn với dầu ăn.
Mắm tôm:
Cho 3 muỗng canh mắm tôm vào chén, thêm 1 muỗng canh đường, 1 quả quất vắt lấy nước cốt, 1 quả ớt tươi băm nhuyễn, 1 muỗng canh dầu ăn, 1 củ hành tím băm nhuyễn, nước cốt chanh và tỏi băm. Khuấy đều hỗn hợp mắm tôm cho đến khi tan đều.
Rau sống: Rửa sạch rau sống, để ráo nước. Ớt tươi cắt lát. Chanh cắt múi cau.
Bước 2: Hoàn thành:

Xếp bún, đậu hũ rán, thịt ba chỉ rán, thịt chân giò rán và rau sống lên đĩa.
Dùng kèm với mắm tôm, muối tiêu chanh, tương ớt và sa tế."""),
Food(id=17, name='Bún mắm', guide=r"""Nguyên liệu:
Nguyên liệu:

Mắm:

200gr mắm cá linh hoặc cá sặc
1 lít nước lọc
1 muỗng canh đường
1 muỗng cà phê muối
1 muỗng canh sả băm
1 muỗng canh ớt băm
1 muỗng canh tỏi băm
Thịt:

300gr thịt heo quay
300gr tôm sú
200gr mực ống
200gr chả cá thác lác
Rau sống:

Rau sống ăn kèm bún mắm (bắp chuối bào, bông súng, rau muống bào, giá đỗ, rau thơm,...)
Ớt tươi
Chanh
Gia vị:

Muối tiêu chanh
Tương ớt
Sa tế
Dụng cụ:

Nồi lớn
Chảo rán
Dao thớt
Tô chén
Muỗng, vá
Khuôn rán chả cá (hoặc chảo chống dính)
Cách làm:

Bước 1: Sơ chế nguyên liệu:

Mắm: Pha mắm cá linh hoặc cá sặc với nước lọc, đường, muối, sả băm, ớt băm và tỏi băm. Khuấy đều cho đến khi tan hết. Nấu sôi hỗn hợp mắm, sau đó hạ nhỏ lửa và hầm trong khoảng 15 phút cho đến khi mắm sệt lại.
Thịt: Cắt thịt heo quay thành từng miếng vừa ăn. Tôm sú rửa sạch, bóc vỏ, bỏ đầu và chỉ đen. Mực ống rửa sạch, cắt khoanh. Chả cá thác lác chiên vàng giòn.
Rau sống: Rửa sạch rau sống, để ráo nước. Ớt tươi cắt lát. Chanh cắt múi cau.
Bước 2: Hoàn thành:

Xếp bún, thịt heo quay, tôm sú, mực ống, chả cá thác lác và rau sống lên đĩa.
Chan nước mắm đã nấu lên trên.
Dùng kèm với muối tiêu chanh, tương ớt và sa tế."""),
Food(id=18, name='Bún riêu', guide=r"""Nguyên liệu:
Cua đồng: 1kg
Cà chua: 5 quả
Đậu hũ: 3 miếng
Bún tươi: 1,5kg
Giấm bỗng: 1 bát
Rau sống: Rau muống, bắp chuối, giá, húng quế, tía tô
Hành lá, ớt, chanh
Hành khô: 5 củ
Gia vị: Muối, hạt nêm, đường, tiêu
Cách làm:

Bước 1: Sơ chế nguyên liệu:

Cua đồng: Rửa sạch cua đồng, tách mai lấy gạch và thịt cua. Giã nhuyễn phần thịt cua, lọc lấy nước. Cho phần xác cua vào nồi nước, ninh lấy nước dùng. Nêm nếm gia vị cho vừa ăn.
Cà chua: Rửa sạch cà chua, cắt múi cau. Phi thơm hành khô băm với dầu ăn, cho cà chua vào xào chín.
Đậu hũ: Rửa sạch đậu hũ, cắt miếng vừa ăn. Chiên vàng đậu hũ.
Rau sống: Rửa sạch rau sống, để ráo nước. Hành lá cắt nhỏ. Ớt thái lát. Chanh cắt múi cau.
Bước 2: Làm riêu cua:

Cho phần gạch cua vào tô, đánh tan với trứng gà. Nêm nếm gia vị cho vừa ăn.
Khi nước dùng cua sôi, cho từ từ hỗn hợp gạch cua vào nồi, khuấy nhẹ tay để riêu cua nổi lên mặt nước.
Nấu thêm khoảng 5 phút cho riêu cua chín, tắt bếp.
Bước 3: Hoàn thành:

Xếp bún, riêu cua, cà chua xào, đậu hũ chiên vào tô.
Chan nước dùng cua nóng hổi lên trên.
Dùng kèm với rau sống, hành lá, ớt, chanh và giấm bỗng."""),
Food(id=19, name='Bún thịt nướng', guide=r"""Nguyên liệu:
Thịt:

1 kg thịt nạc vai
1 muỗng canh hành tím băm
1.5 muỗng canh tỏi băm
1/2 muỗng cà phê ngũ vị hương
1 muỗng canh dầu hào
2 muỗng canh mật ong
1 muỗng canh nước màu
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
1 muỗng canh dầu ăn
Nước mắm:

900ml nước
280g đường
36g muối hột
80g nước mắm 40 độ đạm
1 muỗng canh giấm
1 muỗng cà phê bột ngọt
Rau sống:

Xà lách, rau thơm, dưa leo
Ớt tươi
Chanh
Gia vị:

Muối tiêu chanh
Tương ớt
Sa tế
Dụng cụ:

Nồi lớn
Chảo rán
Dao thớt
Tô chén
Muỗng, vá
Khuôn rán đậu hũ (hoặc chảo chống dính)
Giấy nến
Cách nấu:

Bước 1: Sơ chế nguyên liệu:

Thịt: Rửa sạch thịt nạc vai, cắt thành từng miếng mỏng vừa ăn. Ướp thịt với hành tím băm, tỏi băm, ngũ vị hương, dầu hào, mật ong, nước màu, muối, tiêu và dầu ăn trong ít nhất 30 phút cho thịt thấm gia vị.
Nước mắm: Pha nước mắm với nước, đường, muối hột, nước mắm, giấm và bột ngọt. Nấu sôi nước mắm, hớt bọt, sau đó để nguội.
Rau sống: Rửa sạch rau sống, để ráo nước. Ớt tươi cắt lát. Chanh cắt múi cau.
Bước 2: Nướng thịt:

Xếp thịt đã ướp vào vỉ nướng hoặc chảo nướng, nướng trên lửa than hoa hoặc bếp nướng điện cho đến khi thịt chín vàng đều.
Bước 3: Hoàn thành:

Xếp bún, thịt nướng, rau sống lên đĩa.
Chan nước mắm đã pha lên trên.
Dùng kèm với muối tiêu chanh, tương ớt và sa tế."""),
Food(id=20, name='Cá kho tộ', guide=r"""Nguyên liệu:
Thịt:

1 kg thịt nạc vai
1 muỗng canh hành tím băm
1.5 muỗng canh tỏi băm
1/2 muỗng cà phê ngũ vị hương
1 muỗng canh dầu hào
2 muỗng canh mật ong
1 muỗng canh nước màu
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
1 muỗng canh dầu ăn
Nước mắm:

900ml nước
280g đường
36g muối hột
80g nước mắm 40 độ đạm
1 muỗng canh giấm
1 muỗng cà phê bột ngọt
Rau sống:

Xà lách, rau thơm, dưa leo
Ớt tươi
Chanh
Gia vị:

Muối tiêu chanh
Tương ớt
Sa tế
Dụng cụ:

Nồi lớn
Chảo rán
Dao thớt
Tô chén
Muỗng, vá
Khuôn rán đậu hũ (hoặc chảo chống dính)
Giấy nến
Cách nấu:

Bước 1: Sơ chế nguyên liệu:

Thịt: Rửa sạch thịt nạc vai, cắt thành từng miếng mỏng vừa ăn. Ướp thịt với hành tím băm, tỏi băm, ngũ vị hương, dầu hào, mật ong, nước màu, muối, tiêu và dầu ăn trong ít nhất 30 phút cho thịt thấm gia vị.
Nước mắm: Pha nước mắm với nước, đường, muối hột, nước mắm, giấm và bột ngọt. Nấu sôi nước mắm, hớt bọt, sau đó để nguội.
Rau sống: Rửa sạch rau sống, để ráo nước. Ớt tươi cắt lát. Chanh cắt múi cau.
Bước 2: Nướng thịt:

Xếp thịt đã ướp vào vỉ nướng hoặc chảo nướng, nướng trên lửa than hoa hoặc bếp nướng điện cho đến khi thịt chín vàng đều.
Bước 3: Hoàn thành:

Xếp bún, thịt nướng, rau sống lên đĩa.
Chan nước mắm đã pha lên trên.
Dùng kèm với muối tiêu chanh, tương ớt và sa tế."""),
Food(id=21, name='Canh chua', guide=r"""Nguyên liệu:
Cá lóc: 500gr
Dứa (thơm): 1/2 trái
Cà chua: 2 quả
Đậu bắp: 100gr
Giá đỗ: 100gr
Me chua: 2 quả
Hành lá, ngò gai: 1 ít
Ớt: 2-3 quả
Tỏi: 5 tép
Gia vị: Muối, đường, hạt nêm, nước mắm, dầu ăn
Dụng cụ:

Nồi nấu canh
Dao thớt
Tô chén
Muỗng, vá
Cách nấu:

Bước 1: Sơ chế nguyên liệu:

Cá lóc: Rửa sạch cá lóc, cắt khúc vừa ăn. Ướp cá với 1 muỗng cà phê muối, 1/2 muỗng cà phê tiêu trong 15 phút.
Dứa (thơm): Gọt vỏ, bỏ mắt, cắt miếng vừa ăn.
Cà chua: Rửa sạch cà chua, bổ múi cau.
Đậu bắp: Rửa sạch đậu bắp, cắt bỏ đầu đuôi.
Giá đỗ: Rửa sạch giá đỗ.
Me chua: Ngâm me chua với nước ấm, lọc lấy nước cốt.
Hành lá, ngò gai: Rửa sạch, cắt nhỏ.
Ớt: Bỏ hạt, cắt lát.
Tỏi: Bóc vỏ, băm nhuyễn.
Bước 2: Nấu canh:

Phi thơm 1 muỗng canh dầu ăn với hành tím băm, cho cá lóc đã ướp vào xào săn.
Đổ nước vào nồi, nấu sôi.
Cho dứa (thơm), cà chua vào nồi, nấu cho đến khi dứa (thơm) và cà chua chín mềm.
Nêm nếm gia vị với muối, đường, hạt nêm, nước mắm cho vừa ăn.
Cho nước cốt me vào nồi, khuấy đều.
Tiếp tục nấu cho đến khi canh sôi trở lại.
Cho đậu bắp, giá đỗ vào nồi, nấu thêm khoảng 2 phút.
Tắt bếp, cho hành lá, ngò gai cắt nhỏ vào nồi.
Bước 3: Trình bày và thưởng thức:

Múc canh chua cá lóc ra tô, rắc thêm ớt cắt lát lên trên.
Dùng kèm với cơm nóng và rau sống.
Lưu ý:

Nên chọn mua cá lóc tươi ngon để nấu canh được ngon.
Có thể thay đổi loại cá tùy theo sở thích.
Nên nấu canh với lửa nhỏ để cá chín mềm và thấm gia vị.
Có thể thêm vào nồi canh một ít rau thơm khác như rau mùi, rau ngổ,...
Nên ăn canh chua cá lóc khi còn nóng để cảm nhận được vị thanh mát của món canh."""),
Food(id=22, name='Cao lầu', guide=r"""Nguyên liệu:
1. Sợi cao lầu:

200gr mì cao lầu khô (có thể mua ở các cửa hàng đặc sản hoặc tự làm)
100gr mì sợi (bún, mì gạo...)
2. Nước dùng:

500gr xương heo
2 lít nước
1 muỗng canh muối
1/2 muỗng cà phê tiêu
1 củ hành tây
2 củ gừng
2 tép tỏi
3. Thịt xá xíu:

300gr thịt ba chỉ
2 muỗng canh nước tương
1 muỗng canh mật ong
1 muỗng cà phê ngũ vị hương
1/2 muỗng cà phê bột tỏi
1/4 muỗng cà phê tiêu
1 muỗng canh dầu hào
1 muỗng canh dầu ăn
4. Mộc nhĩ:

50gr mộc nhĩ khô
5. Da heo:

100gr da heo
1 muỗng canh nước tương
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
1/4 muỗng cà phê bột tỏi
6. Rau sống:

Rau sống ăn kèm bún mắm (bắp chuối bào, bông súng, rau muống bào, giá đỗ, rau thơm,...)
Ớt tươi
Chanh
7. Gia vị:

Nước mắm
Tương ớt
Sa tế
Muối tiêu chanh
Dụng cụ:

Nồi lớn
Chảo rán
Dao thớt
Tô chén
Muỗng, vá
Khuôn rán da heo (hoặc chảo chống dính)
Cách làm:

1. Sơ chế nguyên liệu:

Sợi cao lầu: Ngâm mì cao lầu khô trong nước ấm khoảng 30 phút cho mềm. Luộc mì cao lầu khô và mì sợi trong nước sôi khoảng 2 phút, vớt ra để ráo nước.
Nước dùng: Rửa sạch xương heo, cho vào nồi cùng nước, hành tây, gừng, tỏi và 1 muỗng canh muối. Hầm xương với lửa nhỏ trong khoảng 2 tiếng cho đến khi nước dùng ngọt thanh. Nêm nếm gia vị cho vừa ăn.
Thịt xá xíu: Cắt thịt ba chỉ thành miếng vừa ăn. Ướp thịt với nước tương, mật ong, ngũ vị hương, bột tỏi, tiêu, dầu hào và dầu ăn trong ít nhất 30 phút cho thịt thấm gia vị. Rán hoặc nướng thịt xá xíu cho chín vàng.
Mộc nhĩ: Ngâm mộc nhĩ khô trong nước ấm khoảng 15 phút cho nở mềm. Cắt bỏ chân nấm, rửa sạch.
Da heo: Rửa sạch da heo, cắt thành miếng vừa ăn. Ướp da heo với nước tương, muối, tiêu và bột tỏi trong ít nhất 15 phút. Chiên da heo giòn.
2. Hoàn thành:

Xếp mì cao lầu và mì sợi vào tô.
Thêm thịt xá xíu, mộc nhĩ, da heo chiên giòn và rau sống lên trên.
Chan nước dùng nóng hổi lên trên.
Dùng kèm với nước mắm, tương ớt, sa tế và muối tiêu chanh.
Lưu ý:

Nên chọn mua mì cao lầu khô chính hãng để có được hương vị thơm ngon nhất.
Có thể thay đổi nguyên liệu thịt xá xíu tùy theo sở thích.
Nên chiên da heo giòn vừa ăn để da heo không bị dai.
Bún cao lầu ăn nóng là ngon nhất."""),
Food(id=23, name='Cháo lòng', guide=r"""Nguyên liệu:
Phủ tạng heo:
500gr lòng non
200gr gan heo
200gr dạ dày heo
200gr tim heo
200gr tiết heo
Lưỡi heo (tùy chọn)
Gạo:
100gr gạo nếp
200gr gạo tẻ
Xương heo: 500gr
Hành lá, ngò gai: 1 ít
Hành tím, ớt: 1 ít
Gia vị: Muối, đường, hạt nêm, nước mắm, tiêu, dầu ăn
Dụng cụ:

Nồi nấu cháo
Dao thớt
Tô chén
Muỗng, vá
Khuôn rán dồi (hoặc chảo chống dính)
Cách làm:

Bước 1: Sơ chế nguyên liệu:

Phủ tạng heo: Rửa sạch lòng non, gan, dạ dày, tim heo và tiết heo. Lòng non có thể tuốt bỏ phần màng trắng bên trong. Gan heo có thể khử mùi tanh bằng cách ngâm với sữa tươi hoặc nước muối loãng. Dạ dày heo có thể luộc sơ và cạo sạch phần màng nhầy bên trong. Tim heo có thể cắt bỏ tim mỡ. Tiết heo có thể khử mùi tanh bằng cách ngâm với nước muối loãng. Lưỡi heo (nếu có) rửa sạch.
Gạo: Vo sạch gạo nếp và gạo tẻ.
Xương heo: Rửa sạch xương heo.
Hành lá, ngò gai: Rửa sạch, cắt nhỏ.
Hành tím, ớt: Băm nhuyễn.
Bước 2: Nấu cháo:

Nấu nước dùng: Cho xương heo vào nồi, đổ nước vào và hầm trong khoảng 2 tiếng cho đến khi nước dùng ngọt thanh. Nêm nếm gia vị với muối cho vừa ăn.
Nấu cháo: Cho gạo nếp và gạo tẻ vào nồi nước dùng, nấu cho đến khi gạo nở mềm.
Luộc lòng non, gan, dạ dày và tim heo: Cho lòng non, gan, dạ dày và tim heo vào nồi nước sôi, luộc chín. Vớt ra để ráo nước.
Làm dồi: Trộn đều tiết heo, lòng non băm, gan băm, dạ dày băm và tim băm với hành tím băm, ớt băm, muối, tiêu và một ít nước dùng. Nhồi hỗn hợp vào lòng non đã luộc chín. Dùng dây buộc chặt hai đầu lòng non.
Chiên dồi: Cho dồi vào chảo dầu nóng, chiên vàng đều các mặt.
Hoàn thành: Xếp cháo ra tô, cho lòng non, gan, dạ dày, tim heo, dồi chiên và hành lá, ngò gai lên trên. Chan thêm nước dùng nóng hổi và thưởng thức."""),
Food(id=24, name='Cơm tấm', guide=r"""Nguyên liệu:
1. Cơm tấm:

500gr gạo tấm
1 muỗng canh muối
1 muỗng canh dầu ăn
2. Sườn nướng:

500gr sườn cốt lết
2 muỗng canh mật ong
1 muỗng canh nước mắm
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
1 muỗng canh dầu hào
1 muỗng canh dầu ăn
1 củ hành tím
2 tép tỏi
1 muỗng canh hành lá băm
3. Bì heo:

200gr bì heo
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
1 muỗng canh thính gạo
1 muỗng canh hành lá băm
4. Trứng ốp la:

2 quả trứng gà
1 muỗng canh dầu ăn
5. Nước mắm chua ngọt:

2 muỗng canh nước mắm
2 muỗng canh đường
1 muỗng canh nước cốt chanh
1/2 muỗng cà phê ớt băm
1/2 muỗng cà phê tỏi băm
6. Đồ chua:

1 củ cải trắng
1 củ cà rốt
1/2 muỗng cà phê muối
1 muỗng canh giấm
1 muỗng canh đường
7. Rau sống:

Xà lách, dưa leo, húng quế, ngò gai
Dụng cụ:

Nồi cơm điện
Lò nướng (hoặc bếp than)
Chảo
Dao thớt
Tô chén
Muỗng, vá
Cách làm:

1. Nấu cơm tấm:

Vo sạch gạo tấm, cho vào nồi cơm điện cùng 1 muỗng canh muối và 1 muỗng canh dầu ăn. Nấu cơm như bình thường.
2. Nướng sườn:

Rửa sạch sườn cốt lết, để ráo nước.
Trộn đều sườn với mật ong, nước mắm, muối, tiêu, dầu hào, dầu ăn, hành tím băm, tỏi băm và hành lá băm. Ướp sườn trong ít nhất 30 phút cho thấm gia vị.
Nướng sườn trên bếp than hoặc trong lò nướng ở 200°C cho đến khi sườn chín vàng đều.
3. Làm bì heo:

Rửa sạch bì heo, luộc chín.
Thái bì heo thành sợi mỏng.
Trộn đều bì heo với muối, tiêu, thính gạo và hành lá băm.
4. Chiên trứng ốp la:

Đập trứng gà vào tô, nêm nếm gia vị cho vừa ăn.
Cho dầu ăn vào chảo, đun nóng.
Cho trứng vào chảo, chiên đến khi lòng trắng chín se, lòng đỏ còn runny.
5. Pha nước mắm chua ngọt:

Trộn đều nước mắm, đường, nước cốt chanh, ớt băm và tỏi băm.
6. Làm đồ chua:

Gọt vỏ củ cải trắng và cà rốt, bào sợi.
Ngâm củ cải trắng và cà rốt trong nước muối loãng khoảng 15 phút.
Vớt củ cải trắng và cà rốt ra, vắt ráo nước.
Trộn đều củ cải trắng, cà rốt với giấm và đường.
7. Hoàn thành:

Xếp cơm tấm ra đĩa, cho sườn nướng, bì heo, trứng ốp la, đồ chua và rau sống lên trên.
Dùng kèm với nước mắm chua ngọt."""),
Food(id=25, name='Gỏi cuốn', guide=r"""Nguyên liệu:
1. Bánh tráng:

200gr bánh tráng cuốn
Nước ấm
2. Nhân cuốn:

300gr thịt ba chỉ
200gr tôm sú
100gr bún tươi
100gr giá đỗ
1 trái dưa leo
1 củ cà rốt
1 củ hành tây
Rau thơm: húng lủi, húng quế, tía tô, rau mùi,...
Ớt, tỏi
3. Nước chấm:

100ml nước mắm ngon
100ml nước lọc
1 muỗng canh đường
1 muỗng canh nước cốt chanh
1 tép tỏi
1/2 quả ớt
Dụng cụ:

Tô, dĩa
Dao thớt
Nồi luộc
Chảo rán
Cách làm:

1. Sơ chế nguyên liệu:

Bánh tráng: Nhúng bánh tráng vào nước ấm cho mềm, vớt ra để ráo nước.
Thịt ba chỉ: Rửa sạch thịt ba chỉ, luộc chín, vớt ra để ráo nước. Cắt thịt ba chỉ thành sợi mỏng.
Tôm sú: Bóc vỏ, bỏ đầu, chỉ đen. Rửa sạch tôm, luộc chín, vớt ra để ráo nước. Cắt tôm thành miếng vừa ăn.
Bún tươi: Chần qua nước sôi cho bún mềm, vớt ra để ráo nước.
Giá đỗ: Rửa sạch giá đỗ.
Dưa leo: Rửa sạch dưa leo, bào sợi.
Cà rốt: Gọt vỏ, bào sợi.
Hành tây: Bóc vỏ, cắt lát mỏng.
Rau thơm: Rửa sạch rau thơm, cắt nhỏ.
Ớt, tỏi: Băm nhuyễn.
2. Pha nước chấm:

Cho nước mắm, nước lọc, đường, nước cốt chanh vào tô, khuấy đều cho tan.
Cho tỏi băm, ớt băm vào tô nước chấm, khuấy đều.
3. Cuốn gỏi:

Trải bánh tráng ra dĩa.
Xếp lần lượt các nguyên liệu lên trên bánh tráng: bún, thịt ba chỉ, tôm sú, giá đỗ, dưa leo, cà rốt, hành tây, rau thơm.
Cuốn bánh tráng lại cho chặt tay.
Tiếp tục cuốn cho đến khi hết nguyên liệu."""),
Food(id=26, name='Hủ tiếu', guide=r"""Nguyên liệu:
1. Nước dùng:

1 kg xương heo
500gr thịt nạc
300gr tôm
200gr mực
200gr giò heo (tùy chọn)
50gr tôm khô
1 củ cải trắng
1 củ hành tây
1 bó hẹ
1 củ gừng
2 tép tỏi
Gia vị: muối, đường, hạt nêm, nước mắm
2. Sợi hủ tiếu:

500gr hủ tiếu dai
100gr hủ tiếu sợi (bún, mì gạo...)
3. Nhân hủ tiếu:

300gr thịt nạc dăm
200gr gan heo
10 quả trứng cút
100gr nấm mèo
100gr giá đỗ
Rau sống: xà lách, húng quế, giá đỗ, hẹ
Ớt, chanh
4. Gia vị:

Nước mắm
Tương ớt
Sa tế
Muối tiêu chanh
Dụng cụ:

Nồi lớn
Chảo rán
Dao thớt
Tô chén
Muỗng, vá
Khuôn rán da heo (hoặc chảo chống dính)
Cách làm:

1. Nấu nước dùng:

Rửa sạch xương heo, cho vào nồi cùng nước, hành tây, gừng, tỏi và 1 muỗng canh muối. Hầm xương với lửa nhỏ trong khoảng 2 tiếng cho đến khi nước dùng ngọt thanh. Nêm nếm gia vị cho vừa ăn.
Luộc thịt nạc, tôm và mực. Vớt ra để ráo nước.
Chiên giò heo (nếu có). Vớt ra để ráo dầu.
Ngâm tôm khô trong nước ấm cho mềm.
Gọt vỏ củ cải trắng, cắt khúc.
Nấm mèo ngâm nước ấm cho nở mềm, cắt bỏ chân.
Cho tôm khô, củ cải trắng, nấm mèo vào nồi nước dùng, hầm thêm khoảng 30 phút.
2. Sơ chế nhân hủ tiếu:

Thịt nạc dăm ướp với tiêu, hạt nêm và 1 muỗng canh nước tương.
Gan heo luộc chín, cắt lát mỏng.
Luộc trứng cút, bóc vỏ.
Giá đỗ rửa sạch.
Rau sống rửa sạch, cắt nhỏ.
Ớt cắt lát, chanh cắt múi cau."""),
Food(id=27, name='Mì quảng', guide=r"""Nguyên liệu:
1. Mì:

500gr mì Quảng sợi tươi
2. Gà:

1 con gà ta (khoảng 1.5kg)
1 muỗng canh bột nghệ
1 muỗng canh dầu điều
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
1/2 muỗng cà phê bột ngọt
Hành lá, ngò gai
3. Nước dùng:

Xương gà (từ con gà đã luộc)
1 lít nước
50gr củ nén
3 củ hành tím
2 muỗng canh nước mắm
1 muỗng canh đường phèn
1 muỗng cà phê muối
1/2 muỗng cà phê tiêu
4. Nhân:

20 quả trứng cút
100gr đậu phộng rang
100gr bánh tráng nướng
Bắp chuối bào
Rau sống: xà lách, húng lủi, giá đỗ
5. Gia vị:

Nước mắm
Ớt, chanh
Dụng cụ:

Nồi nấu
Chảo
Dao thớt
Tô chén
Muỗng, vá
Khuôn rán dồi (hoặc chảo chống dính)
Cách làm:

1. Sơ chế nguyên liệu:

Gà: Rửa sạch gà, chặt miếng vừa ăn. Ướp gà với bột nghệ, dầu điều, muối, tiêu và bột ngọt trong ít nhất 30 phút cho thấm gia vị.
Nước dùng: Luộc gà với nước, củ nén và hành tím trong khoảng 45 phút cho đến khi gà chín mềm. Vớt gà ra để ráo nước. Nêm nếm gia vị cho nước dùng với nước mắm, đường phèn, muối và tiêu.
Trứng cút: Luộc chín trứng cút, bóc vỏ.
Đậu phộng: Rang chín đậu phộng, bóc vỏ, giã dập.
Bánh tráng nướng: Bẻ nhỏ bánh tráng nướng.
Bắp chuối: Bào sợi bắp chuối.
Rau sống: Rửa sạch rau sống, cắt nhỏ.
2. Nấu mì Quảng:

Nấu sôi nước, cho mì Quảng vào chần sơ qua rồi vớt ra để ráo nước.
Cho mì Quảng vào tô.
Xếp gà luộc, trứng cút, đậu phộng rang, bánh tráng nướng, bắp chuối và rau sống lên trên.
Chan nước dùng nóng hổi lên trên.
Dùng kèm với nước mắm, ớt và chanh.
"""),
Food(id=28, name='Nem chua', guide=r"""Nguyên liệu:
Thịt:
1 kg thịt nạc mông heo
200gr bì heo
Gia vị:
100gr thính gạo
50gr tỏi
10 quả ớt
1 muỗng cà phê đường
1 muỗng cà phê muối
1 muỗng cà phê tiêu
1 muỗng canh nước mắm
1 muỗng cà phê rượu trắng
Bột năng (tùy chọn)
Lá gói:
Lá chuối hoặc lá nem chua
Dây chun
Dụng cụ:

Máy xay thịt
Tô, dĩa
Dao thớt
Khuôn ép nem (hoặc chai nhựa)
Găng tay (tùy chọn)
Cách làm:

1. Sơ chế nguyên liệu:

Thịt: Rửa sạch thịt nạc mông heo, để ráo nước. Xay thịt nhuyễn.
Bì heo: Rửa sạch bì heo, luộc chín. Cạo sạch lông và mỡ thừa. Thái bì heo thành sợi nhỏ.
Tỏi: Bóc vỏ, băm nhuyễn.
Ớt: Băm nhuyễn.
Trộn nguyên liệu: Cho thịt xay, bì heo, thính gạo, tỏi băm, ớt băm, đường, muối, tiêu, nước mắm, rượu trắng vào tô lớn. Trộn đều tất cả nguyên liệu cho đến khi hòa quyện.
Nêm nếm gia vị: Nếm thử hỗn hợp nem chua và điều chỉnh gia vị cho vừa ăn.
Thêm bột năng (tùy chọn): Nếu muốn nem chua dai giòn hơn, bạn có thể thêm 1 - 2 muỗng cà phê bột năng vào hỗn hợp nem chua và trộn đều.
2. Gói nem:

Chuẩn bị lá gói: Rửa sạch lá chuối hoặc lá nem chua, để ráo nước.
Cắt lá gói: Cắt lá chuối hoặc lá nem chua thành từng miếng vuông có kích thước phù hợp.
Gói nem: Cho một lượng vừa đủ hỗn hợp nem chua vào giữa miếng lá gói. Dùng tay nặn nem thành hình trụ dài. Gấp hai đầu lá gói lại và buộc chặt bằng dây chun.
Lặp lại thao tác gói nem cho đến khi hết nguyên liệu.
3. Ủ nem:

Xếp nem vào hộp hoặc hũ.
Đậy kín nắp hộp hoặc hũ.
Ủ nem ở nơi thoáng mát, tránh ánh nắng trực tiếp trong khoảng 2 - 3 ngày."""),
Food(id=29, name='Phở', guide=r"""Nguyên liệu:
1. Nước dùng:

2kg xương bò (gồm: xương ống, đuôi, nạm)
1kg thịt bò (gồm: bắp, nạm, gầu)
1 củ hành tây
4 tép gừng
2 củ hành tím
1 bó hẹ
2 hoa hồi
2 thảo quả
3 đinh hương
1 thanh quế
1 muỗng canh muối
1 muỗng cà phê đường phèn
2. Bánh phở:

1kg bánh phở tươi
3. Thịt:

500gr thịt bò tái
500gr thịt bò chín
4. Gia vị:

Rau thơm: húng quế, ngò gai, giá đỗ, hành lá
Ớt, chanh
Nước mắm
Tương ớt
Dấm ớt
Dụng cụ:

Nồi lớn
Chảo
Dao thớt
Tô chén
Muỗng, vá
Khuôn rán da heo (hoặc chảo chống dính)
Cách làm:

1. Nấu nước dùng:

Rửa sạch xương bò, chần qua nước sôi để loại bỏ bọt bẩn. Cho xương bò vào nồi, đổ nước xâm xấp mặt xương. Hầm xương với lửa nhỏ trong khoảng 2 tiếng.
Trong lúc hầm xương, nướng hành tây, gừng, hành tím và hẹ trên lửa cho đến khi thơm.
Sau 2 tiếng hầm xương, cho thịt bò, hành tây nướng, gừng nướng, hành tím nướng, hẹ nướng, hoa hồi, thảo quả, đinh hương, quế vào nồi. Hầm thêm khoảng 1 tiếng cho đến khi thịt bò chín mềm.
Nêm nếm gia vị với muối và đường phèn cho vừa ăn.
Hớt bỏ bọt và váng mỡ trên mặt nước dùng.
Lọc nước dùng qua rây để loại bỏ xương và xác thịt.
2. Sơ chế nguyên liệu:

Thịt bò: Rửa sạch thịt bò tái và thịt bò chín. Thái thịt bò thành từng lát mỏng.
Rau thơm: Rửa sạch rau thơm, cắt nhỏ.
Ớt: Băm nhuyễn ớt.
Chanh: Cắt chanh thành múi cau.
3. Hoàn thành:

Trụng bánh phở qua nước sôi cho mềm.
Xếp bánh phở vào tô.
Xếp thịt bò tái, thịt bò chín, rau thơm lên trên.
Chan nước dùng nóng hổi lên trên.
Dùng kèm với nước mắm, tương ớt, dấm ớt, ớt băm và chanh."""),
Food(id=30, name='Xôi xéo', guide=r"""Nguyên liệu:
Gạo nếp: 500gr (nên chọn nếp cái hoa vàng)
Đậu xanh cà vỏ: 200gr
Bột nghệ: ½ muỗng cà phê
Muối: ¼ muỗng cà phê
Mỡ gà hoặc mỡ heo: 100gr
Hành tím: 100gr
Gia vị: muối, đường, nước mắm
Cách làm:

1. Sơ chế nguyên liệu:

Gạo nếp: Vo sạch gạo nếp, ngâm gạo với nước và ½ muỗng cà phê muối trong khoảng 8 tiếng.
Đậu xanh cà vỏ: Vo sạch đậu xanh, loại bỏ hạt lép. Ngâm đậu xanh trong nước khoảng 3 - 4 tiếng.
Hành tím: Bóc vỏ, thái lát mỏng.
Mỡ gà hoặc mỡ heo: Rửa sạch mỡ gà hoặc mỡ heo, cắt thành từng miếng nhỏ.
2. Nấu xôi:

Vớt gạo nếp ra, để ráo nước. Cho gạo nếp vào nồi, thêm ½ muỗng cà phê bột nghệ, trộn đều.
Cho nước vào nồi, lượng nước xâm xấp mặt gạo. Nấu xôi với lửa nhỏ cho đến khi xôi chín mềm.
Trong lúc nấu xôi, hấp đậu xanh chín mềm.
Khi xôi chín, cho đậu xanh đã hấp chín vào nồi xôi, đảo đều cho xôi và đậu xanh hòa quyện.
Thêm 2 muỗng canh mỡ gà hoặc mỡ heo vào nồi xôi, đảo đều cho xôi bóng và dẻo mịn.
3. Phi hành:

Cho mỡ gà hoặc mỡ heo vào chảo, phi thơm hành tím.
Khi hành tím vàng giòn, tắt bếp."""),
]

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all(data)
    db.session.commit()